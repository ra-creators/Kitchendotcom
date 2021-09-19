from django.db import models

# Create your models here.
class Blog(models.Model):
    Coverimage = models.FileField(upload_to="")
    Author = models.CharField()
    Content = models.TextField()

class News(models.Model):
    Coverimage = models.FileField(upload_to="")
    Author = models.CharField()
    Content = models.TextField()
