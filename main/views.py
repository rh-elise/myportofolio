from django.contrib import messages
from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from main.forms import ProjectForm
from main.models import Artworks, Experience, Projects

# ---------------------------------------------------------------------------
# Shared profile context
# ---------------------------------------------------------------------------
PROFILE = {
    "name": "Rheina Uliana",
    "npm": "2506600801",
    "study_program": "S1 Sistem Informasi",
    "bio": "Creating with Ristek :D",
    "linkedin": "https://linkedin.com/in/rheinauliana",
    "twitter": "https://x.com/chrobloss",
    "github": "https://github.com/rh-elise",
    "itchio": "https://eeliseee.itch.io",
    "gmail": "rheina.ul67@gmail.com",
    "tagline": "Hi! Hello! How are you?",
}


def _artworks_by_category() -> dict[str, list[Artworks]]:
    """Kelompokkan Artworks berdasarkan category (case-sensitive, trim)."""
    groups: dict[str, list[Artworks]] = {}
    for art in Artworks.objects.all().order_by("id"):
        name = (art.category or "uncategorized").strip() or "uncategorized"
        groups.setdefault(name, []).append(art)
    return groups


def _artwork_context(category_slug: str) -> dict:
    """Bangun konteks tabs + artworks aktif untuk artworks & index."""
    groups = _artworks_by_category()
    slug_to_name = {slugify(name): name for name in groups}

    categories = [
        {"name": name, "slug": slug}
        for slug, name in sorted(slug_to_name.items(), key=lambda kv: kv[1].lower())
    ]

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


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        **PROFILE,
        "projects_list": Projects.objects.all(),
    }
    context.update(_artwork_context(request.GET.get("category", "")))
    return render(request, "index.html", context)


def show_experience(request: HttpRequest) -> HttpResponse:
    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_artworks(request: HttpRequest) -> HttpResponse:
    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
    }
    context.update(_artwork_context(request.GET.get("category", "")))
    return render(request, "artworks.html", context)


def show_projects(request: HttpRequest) -> HttpResponse:
    """Daftar projects dengan filter judul via query param ?title=."""
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)


def get_projects_json(request: HttpRequest) -> HttpResponse:
    """API JSON untuk projects - dipakai filter & testing."""
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = serializers.serialize("json", projects)
    return HttpResponse(data, content_type="application/json")


def create_project(request: HttpRequest) -> HttpResponse:
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added!")
        return redirect("main:show_projects")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "projects_form.html", context)


def delete_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
    return redirect("main:show_projects")
