from django import forms
from django.conf import settings
from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Projects, Experience


class ProjectForm(ModelForm):
    """Form tambah project - validasi agar data konsisten."""

    passcode = forms.CharField(
        label="Passcode",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter passcode to submit"}),
    )

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
        image = self.cleaned_data["image"].strip() if self.cleaned_data["image"] else ""
        if image and not (image.startswith("/static/") or image.startswith("http")):
            raise forms.ValidationError("Cover must be a /static/... path or http(s) URL.")
        return image

    def clean_passcode(self) -> str:
        if self.cleaned_data["passcode"] != settings.PORTFOLIO_PASSCODE:
            raise forms.ValidationError("Wrong passcode.")
        return self.cleaned_data["passcode"]


class ExperienceForm(ModelForm):
    """Form tambah experience - validasi agar data konsisten."""

    passcode = forms.CharField(
        label="Passcode",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter passcode to submit"}),
    )

    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail", "year", "status"]
        labels = {
            "title": "Experience Title",
            "description": "Experience Description",
            "category": "Experience Category",
            "thumbnail": "Experience Thumbnail",
            "year": "Experience Year",
            "status": "Experience Status",
        }

        widgets = {
            "title": TextInput(attrs={
                "placeholder": "What's this experience called?",
                "maxlength": 255,
            }),
            "description": Textarea(attrs={
                "placeholder": "Tell a little about this experience...",
                "rows": 3,
            }),
            "thumbnail": TextInput(attrs={
                "placeholder": "/static/img/experience-cover.png or http(s) URL",
            }),
        }

    def clean_title(self) -> str:
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

    def clean_thumbnail(self) -> str:
        thumbnail = self.cleaned_data["thumbnail"].strip() if self.cleaned_data["thumbnail"] else ""
        if thumbnail and not (thumbnail.startswith("/static/") or thumbnail.startswith("http")):
            raise forms.ValidationError("Cover must be a /static/... path or http(s) URL.")
        return thumbnail

    def clean_passcode(self) -> str:
        if self.cleaned_data["passcode"] != settings.PORTFOLIO_PASSCODE:
            raise forms.ValidationError("Wrong passcode.")
        return self.cleaned_data["passcode"]