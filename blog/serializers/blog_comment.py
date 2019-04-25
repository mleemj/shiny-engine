from rest_framework import serializers

from blog.models.blog_comment import BlogComment


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"
