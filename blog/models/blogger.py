from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=400, blank=True, help_text="Enter your bio details here."
    )

    class Meta:
        ordering = ["user", "bio"]

    def get_absolute_url(self):
        return reverse("blogs-by-author", args=[str(self.id)])

    def __str__(self):
        return self.user.username
