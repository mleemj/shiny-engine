from rest_framework import serializers

from blog.models.blog import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("name", "description")
