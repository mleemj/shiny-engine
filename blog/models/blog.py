from datetime import date

from django.db import models
from django.shortcuts import reverse

from blog.models.blogger import Blogger


class Blog(models.Model):
    name = models.CharField(max_length=200)
    blogger = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        max_length=2000, help_text="Enter your blog text here"
    )
    post_date = models.DateField(default=date.today, auto_created=True)

    class Meta:
        ordering = ["post_date"]
        permissions = (("can_add_comment", "Add comment to blog"),)

    def get_absolute_url(self):
        # id = models.AutoField(primary_key=True)
        return reverse("blog-detail", args=[str(self.id)])

    def __str__(self):
        return self.name
