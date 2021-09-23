from django.db import models
from ckeditor.fields import RichTextField

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

