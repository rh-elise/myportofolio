import uuid

from django.db import models


class Projects(models.Model):
    """Game/project showcase.

    Note: nama model dipertahankan jamak (Projects) untuk kompatibilitas
    migrasi dan tests yang sudah ada.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, help_text="Path statis, mis. /static/img/cover-*.png")
    link = models.URLField(max_length=255, blank=True, help_text="URL eksternal menuju game")

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title


class Artworks(models.Model):
    """Karya visual - kategori bebas, tab halaman mengikuti isi database."""

    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, help_text="Kosong jika berupa video")
    video = models.CharField(max_length=255, blank=True, help_text="Kosong jika berupa gambar")
    category = models.CharField(max_length=50, default="uncategorized")

    class Meta:
        verbose_name_plural = "Artworks"
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title


class Experience(models.Model):
    """Riwayat pengalaman dengan status ongoing/completed."""

    class Category(models.TextChoices):
        INTERNSHIP = "internship", "Internship"
        RESEARCH = "research", "Research"
        VOLUNTEER = "volunteer", "Volunteer"
        PART_TIME = "part-time", "Part-Time"
        FULL_TIME = "full-time", "Full-Time"
        FREELANCE = "freelance", "Freelance"

    class Status(models.TextChoices):
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.FULL_TIME)
    thumbnail = models.URLField(blank=True, null=True)
    year = models.PositiveIntegerField(default=2026)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ONGOING)

    class Meta:
        ordering = ["-year", "title"]

    def __str__(self) -> str:
        return self.title

    @property
    def is_ongoing(self) -> bool:
        return self.status == self.Status.ONGOING
