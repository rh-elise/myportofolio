from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Projects

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "image",
            "link",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "image": "Cover Proyek",
            "link": "Link Proyek"
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Where Do You Belong?",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "A puzzle deduction game where you work as a train conductor guiding living passengers and lost souls to where they belong. Inspect identities by day, uncover the dead by night, and make every decision count.",
                    "rows": 3,
                }
            ),
            "image": TextInput(
                attrs={
                    "placeholder": "/static/img/cover-where-do-you-belong.png",
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://mir4na.itch.io/where-do-you-belong",
                }
            ),
        }