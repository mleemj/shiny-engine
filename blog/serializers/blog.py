from rest_framework import serializers

from blog.models.blog import Blog


class BlogSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=2000, required=True)

    class Meta:
        model = Blog
        fields = ("name", "description")
