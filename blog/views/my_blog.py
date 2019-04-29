from django.forms import formset_factory
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.form.my_blog import MyBlogForm
from blog.models.blog import Blog
from blog.models.blogger import Blogger

BlogFormSet = formset_factory(MyBlogForm, can_delete=True, extra=0)


class MyBlogView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def get(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, user_id=pk)
        blogs = Blog.objects.filter(blogger=blogger)
        formset = BlogFormSet(initial=blogs.values())

        return Response(
            {"formset": formset, "blogger": blogger}, template_name="blog/my_blog.html"
        )

    def post(self, request, pk, *args, **kwargs):
        blogger = get_object_or_404(Blogger, id=pk)
        formset = BlogFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                blogId = form.cleaned_data.get("id")
                name = form.cleaned_data.get("name")
                description = form.cleaned_data.get("description")
                can_delete = form.cleaned_data.get("DELETE")
                if can_delete:
                    Blog.objects.filter(id=blogId).delete()
                else:
                    Blog.objects.filter(id=blogId).update(name=name, description=description)

        return redirect("blogs-by-author", pk=blogger.id)
