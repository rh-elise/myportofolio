import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, JsonResponse
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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": PROFILE["name"],
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": PROFILE["name"],
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


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
    last_login = request.COOKIES.get('last_login', 'No active login session found')

    context = {
        **PROFILE,
        "projects_list": Projects.objects.all(),
        "experience_list": Experience.objects.all(),
        "last_login": last_login,
    }

    context.update(_artwork_context(request.GET.get("category", "")))
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    experience_list = Experience.objects.all()

    if title_query:
        experience_list = experience_list.filter(title__icontains=title_query)

    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
        "experience_list": experience_list,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def get_experience_json(request):
    """API JSON untuk experience - dipakai filter & testing."""
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for exp in experiences:
        data.append({
            "pk": exp.id,
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "thumbnail": exp.thumbnail,
                "category": exp.category,
                "year": exp.year,
                "status": exp.status,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def create_experience(request: HttpRequest) -> HttpResponse:
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added!")
        return redirect("main:show_experience")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def update_experience(request: HttpRequest, experience_id: int) -> HttpResponse:
    if not request.user.has_perm("main.change_experience"):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated!")
        return redirect("main:show_experience")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request: HttpRequest, experience_id: int) -> HttpResponse:
    if not request.user.is_superuser:
        raise PermissionDenied

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

def show_projects(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    context = {
        "name": PROFILE["name"],
        "tagline": PROFILE["tagline"],
        "projects_list": projects,
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    """API JSON untuk projects - dipakai filter & testing."""
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": project.id,
            "fields": {
                "title": project.title,
                "description": project.description,
                "image": project.image,
                "link": project.link,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def create_project(request: HttpRequest) -> HttpResponse:
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added!")
        return redirect("main:show_projects")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "projects_form.html", context)


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects.."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "New project added!", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def update_project(request: HttpRequest, project_id: int) -> HttpResponse:
    if not request.user.has_perm("main.change_projects"):
        raise PermissionDenied

    project = get_object_or_404(Projects, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated!")
        return redirect("main:show_projects")

    context = {"name": PROFILE["name"], "form": form}
    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def delete_project(request: HttpRequest, project_id: int) -> HttpResponse:
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Projects, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
    return redirect("main:show_projects")


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")