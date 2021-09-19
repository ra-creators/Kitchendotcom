from django.contrib import admin

# Register your models here.
from blogandnews.models import Blog, News

admin.site.register(Blog)
admin.site.register(News)
