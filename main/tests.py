from django.contrib.auth.models import Group, Permission, User
from django.test import TestCase
from django.urls import reverse

from main.models import Artworks, Experience, Projects


class MainPageTest(TestCase):
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_main_page_links_all_sections(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_projects")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_artworks")}"')

    def test_main_page_shows_projects_and_artworks(self):
        Projects.objects.create(
            title="Save the Patient!",
            description="A survival game about a doctor enduring a nonstop three-day shift.",
            image="/static/img/cover-savethepatient.png",
            link="https://depelemon.itch.io/save-the-patient",
        )
        Artworks.objects.create(
            title="Game BG",
            image="/static/img/art-pixel-1.png",
            category="pixel",
        )
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "Save the Patient!")
        self.assertContains(response, "Game BG")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)


class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Teaching Assistant - Calculus (Short Semester)",
            description="Supported student comprehension of fundamental calculus concepts.",
            category="part-time",
            year=2026,
        )

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Teaching Assistant - Calculus (Short Semester)")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="exp-grid"')
        self.assertContains(response, 'id="experience-search-form"')
        self.assertNotContains(response, self.experience.title)

    def test_experience_json(self):
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, '"year": 2026')
        self.assertContains(response, '"status": "ongoing"')

    def test_experience_json_filter(self):
        response = self.client.get(reverse("main:get_experience_json") + "?title=calculus")

        self.assertContains(response, self.experience.title)

        response = self.client.get(reverse("main:get_experience_json") + "?title=tidak-ada")
        self.assertNotContains(response, self.experience.title)

    def test_completed_experience(self):
        self.experience.status = "completed"
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, '"status": "completed"')
        self.assertNotContains(response, "ongoing")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience found.")


class ProjectsTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin", password="pass12345", email="admin@example.com"
        )
        self.client.force_login(self.admin)
        self.project = Projects.objects.create(
            title="Save the Patient!",
            description="A survival game about a doctor enduring a nonstop three-day shift.",
            image="/static/img/cover-savethepatient.png",
            link="https://depelemon.itch.io/save-the-patient",
        )

    def test_projects_page(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, 'id="miniCardsContainer"')
        self.assertContains(response, 'id="project-search-form"')
        self.assertNotContains(response, self.project.title)

    def test_empty_projects_page(self):
        Projects.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "No projects found.")

    def test_create_project_post(self):
        response = self.client.post(reverse("main:create_project"), {
            "title": "Brine and Blade",
            "description": "Roguelite bullet-hell.",
            "image": "/static/img/cover-brine-and-blade.png",
            "link": "https://example.com/brine-and-blade",
        })

        self.assertRedirects(response, reverse("main:show_projects"))
        self.assertTrue(Projects.objects.filter(title="Brine and Blade").exists())

    def test_create_project_ajax_post(self):
        response = self.client.post(reverse("main:create_project_ajax"), {
            "title": "Brine and Blade",
            "description": "Roguelite bullet-hell.",
            "image": "/static/img/cover-brine-and-blade.png",
            "link": "https://example.com/brine-and-blade",
        })

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Projects.objects.filter(title="Brine and Blade").exists())

    def test_create_project_ajax_forbidden_for_anonymous(self):
        self.client.logout()
        response = self.client.post(reverse("main:create_project_ajax"), {
            "title": "Brine and Blade",
            "description": "Roguelite bullet-hell.",
            "image": "/static/img/cover-brine-and-blade.png",
            "link": "https://example.com/brine-and-blade",
        })

        self.assertEqual(response.status_code, 403)
        self.assertFalse(Projects.objects.filter(title="Brine and Blade").exists())

    def test_create_project_ajax_rejects_blank_title(self):
        response = self.client.post(reverse("main:create_project_ajax"), {
            "title": "   ",
            "description": "Roguelite bullet-hell.",
            "image": "/static/img/cover-brine-and-blade.png",
            "link": "https://example.com/brine-and-blade",
        })

        self.assertEqual(response.status_code, 400)
        self.assertIn("title", response.json()["errors"])

    def test_projects_json(self):
        response = self.client.get(reverse("main:get_projects_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertContains(response, self.project.title)
        self.assertContains(response, '"star_count": 0')
        self.assertContains(response, '"is_starred": false')

    def test_projects_json_filter(self):
        response = self.client.get(reverse("main:get_projects_json") + "?title=patient")

        self.assertContains(response, self.project.title)

        response = self.client.get(reverse("main:get_projects_json") + "?title=tidak-ada")
        self.assertNotContains(response, self.project.title)

    def test_projects_search_empty_message(self):
        response = self.client.get(reverse("main:show_projects") + "?title=tidak-ada")

        self.assertContains(response, "No projects found.")

    def test_delete_project_post(self):
        response = self.client.post(reverse("main:delete_project", args=[self.project.id]))

        self.assertRedirects(response, reverse("main:show_projects"))
        self.assertFalse(Projects.objects.filter(pk=self.project.pk).exists())

    def test_delete_project_get_does_nothing(self):
        response = self.client.get(reverse("main:delete_project", args=[self.project.id]))

        self.assertRedirects(response, reverse("main:show_projects"))
        self.assertTrue(Projects.objects.filter(pk=self.project.pk).exists())

    def test_create_project_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("main:create_project"))

        self.assertRedirects(response, "/login/?next=/projects/add/")

    def test_create_project_forbidden_for_normal_user(self):
        self.client.logout()
        User.objects.create_user(username="user", password="pass12345")
        self.client.login(username="user", password="pass12345")
        response = self.client.get(reverse("main:create_project"))

        self.assertEqual(response.status_code, 403)

    def login_as_editor(self):
        group, _ = Group.objects.get_or_create(name="Editor")
        group.permissions.add(
            Permission.objects.get(codename="change_projects"),
            Permission.objects.get(codename="change_experience"),
        )
        editor = User.objects.create_user(username="editor", password="pass12345")
        editor.groups.add(group)
        self.client.force_login(editor)

    def test_editor_cannot_open_add_project(self):
        self.login_as_editor()
        response = self.client.get(reverse("main:create_project"))

        self.assertEqual(response.status_code, 403)

    def test_editor_cannot_create_project(self):
        self.login_as_editor()
        response = self.client.post(reverse("main:create_project"), {
            "title": "Brine and Blade",
            "description": "Roguelite bullet-hell.",
            "image": "/static/img/cover-brine-and-blade.png",
            "link": "https://example.com/brine-and-blade",
        })

        self.assertEqual(response.status_code, 403)
        self.assertFalse(Projects.objects.filter(title="Brine and Blade").exists())

    def test_editor_can_update_project(self):
        self.login_as_editor()
        response = self.client.post(reverse("main:update_project", args=[self.project.id]), {
            "title": "Save the Patient! (Remastered)",
            "description": self.project.description,
            "image": self.project.image,
            "link": self.project.link,
        })

        self.assertRedirects(response, reverse("main:show_projects"))
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Save the Patient! (Remastered)")

    def test_editor_cannot_delete_experience(self):
        experience = Experience.objects.create(
            title="Teaching Assistant - Calculus",
            description="Supported student comprehension.",
            category="part-time",
            year=2026,
        )
        self.login_as_editor()
        response = self.client.post(reverse("main:delete_experience", args=[experience.id]))

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Experience.objects.filter(pk=experience.pk).exists())

    def test_toggle_star_post(self):
        response = self.client.post(reverse("main:toggle_star", args=[self.project.id]))

        self.assertRedirects(response, reverse("main:show_projects"))
        self.assertTrue(self.project.starred_by.filter(pk=self.admin.pk).exists())

    def test_toggle_star_requires_login(self):
        self.client.logout()
        response = self.client.post(reverse("main:toggle_star", args=[self.project.id]))

        self.assertRedirects(response, f"/login/?next=/projects/{self.project.id}/star/")


class ArtworksTest(TestCase):
    def setUp(self):
        self.artwork = Artworks.objects.create(
            title="Game BG",
            image="/static/img/art-pixel-1.png",
            category="pixel",
        )

    def test_artworks_page(self):
        response = self.client.get(reverse("main:show_artworks"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artworks.html")
        self.assertContains(response, self.artwork.title)

    def test_artworks_category_filter(self):
        Artworks.objects.create(
            title="Portrait",
            image="/static/img/art-mono-1.jpg",
            category="monochrome",
        )
        response = self.client.get(reverse("main:show_artworks") + "?category=monochrome")

        self.assertContains(response, "Portrait")
        self.assertNotContains(response, self.artwork.title)

    def test_new_category_appears_as_tab(self):
        Artworks.objects.create(
            title="Sketch",
            image="/static/img/art-mono-1.jpg",
            category="Sketches",
        )
        response = self.client.get(reverse("main:show_artworks"))

        self.assertContains(response, "Sketches")
        self.assertContains(response, "?category=sketches")

    def test_unknown_category_falls_back_to_first(self):
        response = self.client.get(reverse("main:show_artworks") + "?category=tidak-ada")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.artwork.title)

    def test_empty_artworks_page(self):
        Artworks.objects.all().delete()
        response = self.client.get(reverse("main:show_artworks"))

        self.assertContains(response, "No artworks have been added yet.")
