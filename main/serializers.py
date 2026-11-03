from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Projects


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "description",
            "image",
            "link",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = [
            "id",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]

    def validate_title(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError("Title cannot be empty.")

        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")

        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_image(self, value):
        if value and not (value.startswith("/static/") or value.startswith("http")):
            raise serializers.ValidationError("Cover must be a /static/... path or http(s) URL.")

        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return obj.starred_by.filter(id=request.user.id).exists()

    def get_starred_by_names(self, obj):
        return ", ".join(obj.starred_by.values_list("username", flat=True))


class ExperienceSerializer(serializers.ModelSerializer):
    """Representasi dan validasi data Experience untuk API /api/v1/experience/."""

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id",
            "title",
            "description",
            "category",
            "thumbnail",
            "year",
            "status",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = [
            "id",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]

    def validate_title(self, value):
        value = strip_tags(value).strip()

        if not value:
            raise serializers.ValidationError("Title cannot be empty.")

        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")

        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_thumbnail(self, value):
        value = (value or "").strip()

        if value and not (value.startswith("/static/") or value.startswith("http")):
            raise serializers.ValidationError(
                "Thumbnail must be a /static/... path or http(s) URL."
            )

        return strip_tags(value)

    def get_star_count(self, obj):
        return len(obj.starred_by.all())

    def get_is_starred(self, obj):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            return False

        return any(user.id == request.user.id for user in obj.starred_by.all())

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
