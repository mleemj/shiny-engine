from factory.django import DjangoModelFactory
import factory

from blog.models.blog import Blog
from blog.factory.blogger import BloggerFactory


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    name = factory.Sequence(lambda n: "Blog #%s" % n)
    description = factory.Sequence(lambda n: "Blog description #%s" % n)
    blogger = factory.SubFactory(BloggerFactory)
