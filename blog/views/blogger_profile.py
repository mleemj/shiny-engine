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
        user = get_object_or_404(User, pk=pk)
        blogger = Blogger.objects.get(user=user)
        serializer = BloggerSerializer(blogger)
        return Response(
            {"serializer": serializer, "blogger": blogger.user},
            template_name="blog/blogger_profile.html",
        )

    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        bio = request.data.get("bio")
        Blogger.objects.filter(user=user).update(bio=bio)
        return redirect("blogs-by-author", pk=pk)
