from django.urls import path

from main.views import (
    register,
    login_user,
    logout_user,

    show_main,
    show_artworks,
    show_experience,
    toggle_star,
    show_projects,

    create_experience,
    delete_experience,
    update_experience,
    get_experience_json,

    create_project,
    delete_project,
    update_project,
    get_projects_json,
)

app_name = "main"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("artworks/", show_artworks, name="show_artworks"),
    path("projects/", show_projects, name="show_projects"),

    path("projects/add/", create_project, name="create_project"),
    path("projects/<int:project_id>/edit/", update_project, name="update_project"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path(
        "projects/<int:project_id>/star/",
        toggle_star,
        name="toggle_star",
    ),
    path("api/projects/", get_projects_json, name="get_projects_json"),


    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<int:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<int:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
]
