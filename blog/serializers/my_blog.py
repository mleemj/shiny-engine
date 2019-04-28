from rest_framework import serializers


class MyBlogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    to_delete = serializers.BooleanField(default=False)
    absolute_url = serializers.URLField(read_only=True)
