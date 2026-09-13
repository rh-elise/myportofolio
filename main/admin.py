from django.contrib import admin

from main.models import Artworks, Experience, Projects


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "link")


@admin.register(Artworks)
class ArtworksAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "status")
    list_filter = ("category", "status")
