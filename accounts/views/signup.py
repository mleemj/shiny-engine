from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models.blogger import Blogger


class SignupView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(
            {"form": UserCreationForm()}, template_name="accounts/signup.html"
        )

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password1"]
        user_exists = User.objects.filter(username=username).exists()
        if user_exists is False:
            user = User.objects.create_user(username=username, password=password)
        else:
            user = User.objects.get_by_natural_key(username=username)
        DIY_GROUP_ID = 1
        diy_group = Group.objects.get(id=DIY_GROUP_ID)
        blogger = Blogger.objects.update_or_create(user=user)
        diy_group.user_set.add(user)

        return HttpResponseRedirect(
            redirect_to=reverse("login")
        )  # Redirect to django.contrib.auth.models path('login/', views.LoginView.as_view(), name='login'),
