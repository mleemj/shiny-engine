from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from blog.factory.blog import BlogFactory
from blog.factory.blogger import BloggerFactory
from blog.models.blog import Blog
from blog.serializers.blog import BlogSerializer


class TestMyBlog(APITestCase):
    def test_serialize_model(self):
        blogger = BloggerFactory()
        blog1 = BlogFactory(blogger=blogger)
        blog2 = BlogFactory(blogger=blogger)
        b1 = Blog.objects.get(id=blog1.id)
        count = Blog.objects.count()
        self.assertEqual(b1.description, blog1.description)
        self.assertEqual(count, 2)
        self.assertEqual(blog2.blogger, blog1.blogger)
        qs = Blog.objects.filter(blogger=blogger)
        self.assertEqual(len(qs), 2)
        serializer = BlogSerializer(data=list(qs.values()), many=True)
        serializer.is_valid(raise_exception=True)
        response = Response(
            {"serializer": serializer, "blogger": blogger},
            template_name="blog/my_blog.html",
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
