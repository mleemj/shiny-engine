from django.db import models

from blog.models.blog import Blog
from blog.models.blogger import Blogger


class BlogComment(models.Model):
    description = models.TextField(
        max_length=1000, help_text="Enter comment about blog here."
    )
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        MAX_TITLE_LENGTH = 75
        if len(self.description) > MAX_TITLE_LENGTH:
            titlestring = self.description[:MAX_TITLE_LENGTH] + "..."
        else:
            titlestring = self.description
        return titlestring
