from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blogger import Blogger


class BloggerListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        bloggers = Blogger.objects.all()
        return Response(
            {"blogauthor_list": bloggers}, template_name="blog/blogauthor_list.html"
        )
