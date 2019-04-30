from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from oauth2_provider.views import ProtectedResourceView

from blog.models.blogger import Blogger
from blog.serializers.blogger import BloggerSerializer


class APIEndpoint(ProtectedResourceView):
    """Test OAuth workflow
    When trying to access the API using a browser, there will be a 403 authorization error.

    Get access token using client_credentials grant type
    curl -u <client-id>:<client-secret> http://localhost:8000/o/token/ -d 'grant_type=client_credentials>'

    Use access token to access protected resource
    curl -X GET --header "Authorization: Bearer <access-token>" "http://127.0.0.1:8000/diy/api/profile/1"

    For authorization code grant type, checkout the flask-app
    """

    def get(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, id=pk)
        serializer = BloggerSerializer(blogger)
        return JsonResponse(serializer.data)
