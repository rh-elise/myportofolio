from django.contrib import messages
from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from main.forms import ProjectForm, ExperienceForm
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
        "experience_list": Experience.objects.all(),
    }
    context.update(_artwork_context(request.GET.get("category", "")))
    return render(request, "index.html", context)


def show_experience(request: HttpRequest) -> HttpResponse:
    json_response = get_experience_json(request)
    exps = [e.object for e in serializers.deserialize("json", json_response.content.decode("utf-8"))]
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
        "experience_list": exps,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def get_experience_json(request: HttpRequest) -> HttpResponse:
    """API JSON untuk experience - dipakai filter & testing."""
    title_query = request.GET.get("title", "").strip()
    qs = Experience.objects.all()
    if title_query:
        qs = qs.filter(title__icontains=title_query)
    data = serializers.serialize("json", qs)
    return HttpResponse(data, content_type="application/json")


def create_experience(request: HttpRequest) -> HttpResponse:
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added!")
        return redirect("main:show_experience")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "experience_form.html", context)


def update_experience(request: HttpRequest, experience_id: int) -> HttpResponse:
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated!")
        return redirect("main:show_experience")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "experience_form.html", context)


def delete_experience(request: HttpRequest, experience_id: int) -> HttpResponse:
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully!")
    return redirect("main:show_experience")


def show_artworks(request: HttpRequest) -> HttpResponse:
    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
    }
    context.update(_artwork_context(request.GET.get("category", "")))
    return render(request, "artworks.html", context)


def show_projects(request: HttpRequest) -> HttpResponse:
    json_response = get_projects_json(request)
    projects = [p.object for p in serializers.deserialize("json", json_response.content.decode("utf-8"))]
    title_query = request.GET.get("title", "").strip()
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


def update_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = get_object_or_404(Projects, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated!")
        return redirect("main:show_projects")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "projects_form.html", context)


def delete_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = get_object_or_404(Projects, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
    return redirect("main:show_projects")
