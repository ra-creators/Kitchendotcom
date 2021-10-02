from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogandnews, name="blogandnews"),
    path('blog/<int:blogId>', views.blog, name="blog"),
    # API to post a comment
    path('blogComment', views.blogComment, name="blogComment"),
]