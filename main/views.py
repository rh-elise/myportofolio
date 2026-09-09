from django.shortcuts import render

from main.models import Experience

def show_main(request):
    context = {
        "name": "Rheina Uliana",
        "npm": "2206600801",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Creating with Ristek :D"
        ),
        "linkedin" : "https://linkedin.com/in/rheinauliana",
        "twitter" : "https://x.com/chrobloss",
        "github" : "https://github.com/rh-elise",
        "itchio" : "https://eeliseee.itch.io",
        "gmail" : "rheina.ul67@gmail.com"
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rheina Uliana",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)