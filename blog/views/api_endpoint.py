from django.shortcuts import get_object_or_404
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blogger import Blogger
from blog.serializers.blogger import BloggerSerializer


class APIEndpoint(APIView, ProtectedResourceView):
    """Test OAuth workflow
    Get access token using client-credentials grant type
    curl -u <client-id>:<client-secret> http://localhost:8000/o/token/ -d 'grant_type=client_credentials'

    Get access token using password grant type
    curl -u <client-id>:<client-secret> http://localhost:8000/o/token/ -d 'grant_type=password&username=<username>&password=<password>'

    Use access token to access protected resource
    curl -X GET --header "Authorization: Bearer <access-token>" "http://127.0.0.1:8000/diy/api/profile/1"

    For authorization code grant type, checkout the flask-app
    """
    renderer_classes = [JSONRenderer,]

    def get(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, id=pk)
        serializer = BloggerSerializer(blogger)
        return Response(serializer.data)

