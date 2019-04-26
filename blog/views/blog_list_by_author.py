from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from blog.models.blog import Blog
from blog.models.blogger import Blogger
from blog.serializers.blog import BlogSerializer


class BlogListbyAuthorView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    model = Blog
    paginate_by = 5
    serializer_class = BlogSerializer
    template_name = "blog/blog_list_by_author.html"

    def get(self, request, pk, *args, **kwargs):
        blogger = Blogger.objects.get(Q(id=pk))
        blogs_by_author = Blog.objects.filter(blogger=blogger)
        return Response({"blog_list": blogs_by_author, "blogger": blogger})
