from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from blog.models.blog import Blog


class BlogDetailView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, id=pk)
        return Response({"blog": blog}, template_name="blog/blog_detail.html")
