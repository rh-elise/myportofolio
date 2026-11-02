from django.urls import path

from main.views import (
    create_experience,
    create_experience_ajax,
    create_project,
    create_project_ajax,
    delete_experience,
    delete_project,
    get_experience_json,
    get_projects_json,
    login_user,
    logout_user,
    register,
    show_artworks,
    show_experience,
    show_main,
    show_projects,
    toggle_star,
    update_experience,
    update_project,
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
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/<int:project_id>/edit/", update_project, name="update_project"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),

    path("experience/add/", create_experience, name="create_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<int:experience_id>/edit/", update_experience, name="update_experience"),
    path("experience/<int:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
]
