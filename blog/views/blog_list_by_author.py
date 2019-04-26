from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blog import Blog
from blog.models.blogger import Blogger
from blog.serializers.blog import BlogSerializer


class BlogListbyAuthorView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    model = Blog
    paginate_by = 5
    serializer_class = BlogSerializer
    template_name = "blog/blog_list_by_author.html"

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        blogger = Blogger.objects.get(user=user)
        blogs_by_author = Blog.objects.filter(blogger=blogger.user)
        return Response({"blog_list": blogs_by_author, "blogger": blogger})
