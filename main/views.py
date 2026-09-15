from django.shortcuts import render
from django.utils.text import slugify
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Artworks, Experience, Projects
from main.forms import ProjectForm


# ARTWORKS CATEGORY
def _artworks_by_category():
    groups = {}
    for art in Artworks.objects.all().order_by("id"):
        name = (art.category or "uncategorized").strip() or "uncategorized"
        groups.setdefault(name, []).append(art)
    return groups

# ARTWORKS CATEGORY TABS
def _artwork_context(category_slug):
    # Mengambil kategori
    groups = _artworks_by_category()
    slug_to_name = {slugify(name): name for name in groups}

    # Mengurutkan kategori
    categories = [
        {"name": name, "slug": slug}
        for slug, name in sorted(slug_to_name.items(), key=lambda kv: kv[1].lower())
    ]

    # Menentukan kategori aktif
    if category_slug in slug_to_name:
        active_slug = category_slug
    elif categories:
        active_slug = categories[0]["slug"]
    else:
        active_slug = ""

    return {
        "categories": categories,
        "active_category": active_slug,
        "artworks": groups.get(slug_to_name.get(active_slug, ""), []),
    }

def show_main(request):
    context = {
        "name": "Rheina Uliana",
        "npm": "2506600801",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Creating with Ristek :D"
        ),
        "linkedin" : "https://linkedin.com/in/rheinauliana",
        "twitter" : "https://x.com/chrobloss",
        "github" : "https://github.com/rh-elise",
        "itchio" : "https://eeliseee.itch.io",
        "gmail" : "rheina.ul67@gmail.com",
        "tagline" : "Hi! Hello! How are you?",
        "projects_list": Projects.objects.all(),
    }
    context.update(_artwork_context(request.GET.get("category", "")))

    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rheina Uliana",
        "experience_list": Experience.objects.all(),
        "tagline" : "Hi! Hello! How are you?"
    }
    
    return render(request, "experience.html", context)

def show_artworks(request):
    context = {
        "name": "Rheina Uliana",
        "tagline" : "Hi! Hello! How are you?",
    }
    context.update(_artwork_context(request.GET.get("category", "")))

    return render(request, "artworks.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added!")
        return redirect("main:show_projects")

    context = {
        "name": "Rheina Uliana",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Rheina Uliana",
        "tagline" : "Hi! Hello! How are you?",
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")