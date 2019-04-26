from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blogger import Blogger
from blog.serializers.blog import BlogSerializer


class BlogCreateView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, id=pk)
        blogger = get_object_or_404(Blogger, user_id=user.id)
        serializer = BlogSerializer()
        return Response(
            {"serializer": serializer, "blogger": blogger},
            template_name="blog/blog_create.html",
        )

    def post(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, id=pk)
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(blogger=blogger)

        return redirect("blogs-by-author", pk=blogger.id)
