from rest_framework import serializers

from blog.models.blogger import Blogger


class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ("bio",)
