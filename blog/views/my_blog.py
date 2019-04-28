from django.forms import formset_factory
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.form.my_blog import MyBlogForm
from blog.models.blog import Blog
from blog.models.blogger import Blogger


class MyBlogView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, user_id=pk)
        blogs = Blog.objects.filter(blogger=blogger)
        b1 = {"id": 1, "name": "B1 blog"}
        b2 = {"id": 2, "name": "B2 blog"}
        blog_list = [b1, b2]
        BlogFormSet = formset_factory(MyBlogForm, can_delete=True, extra=0)
        formset = BlogFormSet(
            initial = [
                b1, b2
            ]
        )

        return Response(
            {"form": formset, "blogger": blogger},
            template_name="blog/my_blog.html",
        )

    def post(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, id=pk)
        BlogFormSet = formset_factory(MyBlogForm, can_delete=True, extra=0)
        formset = BlogFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                blogId = form.cleaned_data.get('id')
                can_delete = form.cleaned_data.get('DELETE')
                print('Blog {} Can delete {}'.format( blogId, can_delete))

        return redirect("blogs-by-author", pk=blogger.id)
