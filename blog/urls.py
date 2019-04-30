from django.urls import path

from blog.views.blog_comment import BlogCommentCreate
from blog.views.blog_create import BlogCreateView
from blog.views.blog_detail import BlogDetailView
from blog.views.blog_list import BlogListView
from blog.views.blog_list_by_author import BlogListbyAuthorView
from blog.views.blogger_list import BloggerListView
from blog.views.blogger_profile import BloggerProfileView
from blog.views.index import IndexView
from blog.views.my_blog import MyBlogView
from blog.views.api_endpoint import APIEndpoint
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("blogs/", BlogListView.as_view(), name="blogs"),  # all blogs
    path(
        "blogger/<int:pk>/", BlogListbyAuthorView.as_view(), name="blogs-by-author"
    ),  # pk is blogger_id
    path("blogger/<int:pk>/blogs/", MyBlogView.as_view(), name="my-blog"),
    path(
        "blogger/<int:pk>/blog/", BlogCreateView.as_view(), name="blog-create"
    ),  # pk is user_id
    path(
        "blogger/<int:pk>/profile/",
        BloggerProfileView.as_view(),
        name="blogger-profile",
    ),  # pk is user_id
    path("bloggers/", BloggerListView.as_view(), name="bloggers"),  # all bloggers
    path(
        "blog/<int:pk>", BlogDetailView.as_view(), name="blog-detail"
    ),  # pk is blog_id
    path(
        "blog/<int:pk>/comment/", BlogCommentCreate.as_view(), name="blog-comment"
    ),  # pk is blog_id
    path(
        "api/profile/<int:pk>", APIEndpoint.as_view(), name="apiendpoint"
    )
]
