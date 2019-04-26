from rest_framework import serializers

from blog.models.blog import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("description", "post_date")
        read_only_fields = ("post_date",)
