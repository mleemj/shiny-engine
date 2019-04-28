import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from blog.models.blogger import Blogger


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "User #%s" % n)


class BloggerFactory(DjangoModelFactory):
    class Meta:
        model = Blogger

    user = factory.SubFactory(UserFactory)
    bio = factory.Sequence(lambda n: "Blogger #%s" % n)
