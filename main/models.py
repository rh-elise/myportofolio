import uuid
from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)  # path file
    link = models.CharField(max_length=255, blank=True)  # URL menuju game

    def __str__(self):
        return self.title

class Artworks(models.Model):
    CATEGORY_CHOICES = [
        ('rendered', 'Rendered'),
        ('monochrome', 'Monochrome'),
        ('pixel', 'Pixel'),
        ('animation', 'Animation'),
    ]
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)  # kosong kalau berupa video
    video = models.CharField(max_length=255, blank=True)  # kosong kalau berupa gambar
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='pixel')

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None