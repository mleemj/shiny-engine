from django.urls import path

from blog.views.blog_detail import BlogDetailView
from blog.views.blog_comment import BlogCommentCreate
from blog.views.blog_list import BlogListView
from blog.views.blog_list_by_author import BlogListbyAuthorView
from blog.views.blogger_list import BloggerListView
from blog.views.index import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blogger/<int:pk>", BlogListbyAuthorView.as_view(), name="blogs-by-author"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name="blog-detail"),
    path("bloggers/", BloggerListView.as_view(), name="bloggers"),
    path("blog/<int:pk>/comment/", BlogCommentCreate.as_view(), name="blog_comment"),
]
