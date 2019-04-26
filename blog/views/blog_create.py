from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from blog.serializers.blog import BlogSerializer


class BlogCreateView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, id=pk)
        serializer = BlogSerializer()
        return Response(
            {"serializer": serializer, "blogger": user},
            template_name="blog/blog_create.html",
        )

    def post(self, request, pk, *args, **kwargs):
        return Response(HTTP_201_CREATED)
