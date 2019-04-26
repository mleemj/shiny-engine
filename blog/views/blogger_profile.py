from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blogger import Blogger
from blog.serializers.blogger import BloggerSerializer


class BloggerProfileView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, id=pk)
        blogger = get_object_or_404(Blogger, user=user)
        serializer = BloggerSerializer(blogger)
        return Response(
            {"serializer": serializer, "blogger": blogger.user},
            template_name="blog/blogger_profile.html",
        )

    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, id=pk)
        blogger = get_object_or_404(Blogger, user=user)
        bio = request.data.get("bio")
        blogger.bio = bio
        blogger.save()
        return redirect("blogs-by-author", pk=blogger.id)
