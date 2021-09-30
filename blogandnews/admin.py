from django.contrib import admin
from .models import Blog, News, BlogComment
# Register your models here.

admin.site.register((Blog, BlogComment))
admin.site.register(News)

