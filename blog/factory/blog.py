import factory
from factory.django import DjangoModelFactory

from blog.factory.blogger import BloggerFactory
from blog.models.blog import Blog


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    name = factory.Sequence(lambda n: "Blog #%s" % n)
    description = factory.Sequence(lambda n: "Blog description #%s" % n)
    blogger = factory.SubFactory(BloggerFactory)
