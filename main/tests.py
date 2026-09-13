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
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "2026-present")

    def test_completed_experience(self):
        self.experience.status = "completed"
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "2026")
        self.assertNotContains(response, "present")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")


class ProjectsTest(TestCase):
    def setUp(self):
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
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)

    def test_empty_projects_page(self):
        Projects.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "No projects have been added yet.")


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
