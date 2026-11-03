from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience, Projects


class ProjectAPITest(APITestCase):
    """Test REST API projects memakai model Projects (PK integer)."""

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.project = Projects.objects.create(
            title="Portfolio",
            description="My website",
            image="/static/img/cover-portfolio.png",
            link="https://example.com/",
        )
        self.list_url = reverse("api:project-list")
        self.detail_url = reverse("api:project-detail", args=[self.project.id])
        self.star_url = reverse("api:project-star", args=[self.project.id])
        self.payload = {
            "title": "New project",
            "description": "A useful app",
            "image": "/static/img/cover-new.png",
            "link": "https://example.com/",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.project.id)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "PORT"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_project(self):
        url = reverse("api:project-detail", args=[999999])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            post = self.client.post(self.list_url, self.payload, format="json")
            patch = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
            delete = self.client.delete(self.detail_url)
            self.assertEqual(post.status_code, 403)
            self.assertEqual(patch.status_code, 403)
            self.assertEqual(delete.status_code, 403)
        self.assertEqual(Projects.objects.count(), 1)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Portfolio")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Projects.objects.filter(pk=response.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"title": "   "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"link": "javascript:alert(1)"}, "link"),
            ({"image": ""}, "image"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Projects.objects.count(), 1)

    def test_html_is_stripped_before_saving(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload,
            "title": "<b>Bold</b> title",
            "description": "<b>Hello</b> world",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Bold title")
        self.assertEqual(response.data["description"], "Hello world")

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.description, "My website")
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Projects.objects.filter(pk=self.project.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_and_editor_cannot_manage_projects(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.visitor.groups.add(Group.objects.create(name="Editor"))
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Projects.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # Browsable API merender token CSRF asli di response.
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ExperienceAPITest(APITestCase):
    """Test REST API experience untuk keempat peran dari Tugas 4."""

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )
        self.visitor = User.objects.create_user(
            username="visitor",
            password="test-password",
            email="visitor@example.com",
        )

        editor_group = Group.objects.create(name="Editor")
        editor_group.permissions.add(
            Permission.objects.get(
                codename="change_experience", content_type__app_label="main"
            )
        )
        self.editor = User.objects.create_user(
            username="editor", password="test-password",
        )
        self.editor.groups.add(editor_group)

        self.experience = Experience.objects.create(
            title="Teaching Assistant - Calculus",
            description="Supported student comprehension.",
            category="part-time",
            thumbnail="/static/img/experience-calculus.png",
            year=2026,
            status="ongoing",
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Research Assistant",
            "description": "Helped with data collection.",
            "category": "research",
            "thumbnail": "/static/img/experience-research.png",
            "year": 2025,
            "status": "completed",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.experience.id)
        self.assertEqual(response.data[0]["status"], "ongoing")
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertNotIn("email", response.data[0])
        self.assertNotIn("password", response.data[0])

        detail = self.client.get(self.detail_url)
        self.assertEqual(detail.status_code, status.HTTP_200_OK)
        self.assertEqual(detail.data["title"], self.experience.title)

    def test_search_and_empty_results(self):
        Experience.objects.create(
            title="Volunteer Teacher",
            description="Taught children.",
            category="volunteer",
            year=2024,
        )

        response = self.client.get(self.list_url, {"title": "TEACH"})
        self.assertEqual(len(response.data), 2)

        response = self.client.get(self.list_url, {"title": "assistant"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.experience.title)

        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_experience_returns_404(self):
        url = reverse("api:experience-detail", args=[999999])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            self.client.delete(url).status_code, status.HTTP_403_FORBIDDEN
        )

        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(
            self.client.delete(url).status_code, status.HTTP_404_NOT_FOUND
        )

    def test_guest_and_normal_user_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)

            post = self.client.post(self.list_url, self.payload, format="json")
            put = self.client.put(self.detail_url, self.payload, format="json")
            patch = self.client.patch(
                self.detail_url, {"title": "Changed"}, format="json"
            )
            delete = self.client.delete(self.detail_url)

            self.assertEqual(post.status_code, status.HTTP_403_FORBIDDEN)
            self.assertEqual(put.status_code, status.HTTP_403_FORBIDDEN)
            self.assertEqual(patch.status_code, status.HTTP_403_FORBIDDEN)
            self.assertEqual(delete.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(Experience.objects.count(), 1)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Teaching Assistant - Calculus")

    def test_editor_can_patch_and_put(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url, {"title": "Teaching Assistant (Updated)"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Teaching Assistant (Updated)")
        self.assertEqual(self.experience.description, "Supported student comprehension.")

        response = self.client.put(
            self.detail_url,
            {
                "title": "Teaching Assistant - Calculus II",
                "description": "Graded assignments.",
                "category": "part-time",
                "thumbnail": "",
                "year": 2026,
                "status": "completed",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.status, "completed")

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        post = self.client.post(self.list_url, self.payload, format="json")
        delete = self.client.delete(self.detail_url)

        self.assertEqual(post.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())
        self.assertFalse(Experience.objects.filter(title="Research Assistant").exists())

    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        created = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(created.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Experience.objects.filter(pk=created.data["id"]).exists())

        detail_url = reverse("api:experience-detail", args=[created.data["id"]])
        patched = self.client.patch(
            detail_url, {"title": "Research Assistant (Updated)"}, format="json"
        )
        self.assertEqual(patched.status_code, status.HTTP_200_OK)

        deleted = self.client.delete(detail_url)
        self.assertEqual(deleted.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(deleted.content, b"")
        self.assertFalse(Experience.objects.filter(pk=created.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        for changes, field in [
            ({"title": "   "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"title": "ab"}, "title"),
            ({"thumbnail": "javascript:alert(1)"}, "thumbnail"),
            ({"category": "not-a-category"}, "category"),
            ({"status": "not-a-status"}, "status"),
            ({"year": "not-a-year"}, "year"),
            ({"description": ""}, "description"),
        ]:
            response = self.client.post(
                self.list_url, {**self.payload, **changes}, format="json"
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)

        self.assertEqual(Experience.objects.count(), 1)

    def test_html_is_stripped_before_saving(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "title": "<b>Bold</b> title",
                "description": "<b>Hello</b> world",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Bold title")
        self.assertEqual(response.data["description"], "Hello world")

    def test_star_requires_login_and_toggles_for_request_user(self):
        self.assertEqual(
            self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN
        )

        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.visitor.pk).exists()
        )

        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(
            self.experience.starred_by.filter(pk=self.visitor.pk).exists()
        )

    def test_editor_and_owner_can_star(self):
        for user in (self.editor, self.owner):
            self.client.force_authenticate(user=user)
            response = self.client.post(self.star_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.data["is_starred"])

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "star_count": 99,
                "is_starred": True,
                "starred_by_names": "forged",
                "starred_by": [self.visitor.id],
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["starred_by_names"], "")

    def test_wrong_method_on_list(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))

        response = client.post(self.list_url, self.payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))

        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experience.objects.count(), 2)
