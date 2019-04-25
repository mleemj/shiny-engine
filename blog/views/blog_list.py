from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blog import Blog


class BlogListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return Response({"blog_list": blogs}, template_name="blog/blog_list.html")
