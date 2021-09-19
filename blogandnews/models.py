from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_now=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = models.TextField(default="NA")

    def __str__(self):
        return self.title


class News(models.Model):
    heading = models.CharField(max_length=100, default="Title")
    author = models.CharField(max_length=100, default="admin")
    date = models.DateField(auto_now=True)
    image = models.FileField(upload_to="blogs/", max_length=100)
    content = models.TextField(max_length=1000, default="NA")

    def __str__(self):
        return self.heading

