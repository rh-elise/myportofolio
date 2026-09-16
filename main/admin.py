from django.contrib import admin

from main.models import Artworks, Experience, Projects


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title",)
    list_per_page = 20


@admin.register(Artworks)
class ArtworksAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category",)
    search_fields = ("title", "category")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "status")
    list_filter = ("category", "status")
    search_fields = ("title",)
