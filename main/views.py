from django.shortcuts import render
from django.utils.text import slugify

from main.models import Artworks, Experience, Projects


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

def show_projects(request):
    context = {
        "name": "Rheina Uliana",
        "projects_list": Projects.objects.all(),
        "tagline" : "Hi! Hello! How are you?"
    }

    return render(request, "projects.html", context)