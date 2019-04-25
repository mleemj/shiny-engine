# import model
# add blog to settings.py INSTALLED_APPS
# python manage.py makemigrations blog

from .blog import Blog
from .blog_comment import BlogComment
from .blogger import Blogger
