from django import forms
from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Projects


class ProjectForm(ModelForm):
    """Form tambah project - validasi agar data konsisten."""

    class Meta:
        model = Projects
        fields = ["title", "description", "image", "link"]
        labels = {
                "title": "Project Title",
                "description": "Project Description",
                "image": "Project Cover",
                "link": "Project Link",
            }
        widgets = {
            "title": TextInput(attrs={"placeholder": "What's the project called?", "maxlength": 255}),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell a little story about this project...",
                    "rows": 3,
                }
            ),
            "image": TextInput(attrs={"placeholder": "/static/img/project-cover.png or http(s)/URL"}),
            "link": URLInput(attrs={"placeholder": "https://your-project-link.com"}),
        }

    def clean_title(self) -> str:
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

    def clean_image(self) -> str:
        image = self.cleaned_data["image"].strip()
        if image and not (image.startswith("/static/") or image.startswith("http")):
            raise forms.ValidationError("Cover must be a /static/... path or http(s) URL.")
        return image
