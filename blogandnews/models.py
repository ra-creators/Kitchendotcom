from ast import parse
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_now=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.title


class News(models.Model):
    heading = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_now=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = RichTextField()

    def __str__(self):
        return self.heading

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField(max_length=1000, default="NA")
    name = models.CharField(max_length=50, default="NA")
    email = models.CharField(max_length=32, default="NA")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)