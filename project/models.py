from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    

class Design(models.Model):
    image = models.FileField(upload_to='designs/')

class Feedback(models.Model):
    feedback = models.TextField(max_length=1024, default="NA")
    image = models.FileField(upload_to='feedbacks/')

class Project(models.Model):
    name = models.CharField(max_length=100, null=False, default="Modular Kitchen")
    tagline = models.CharField(max_length=300, default="NA")
    descriptiom = models.TextField(default="NA")
    project_img = models.FileField(upload_to='projects/')
    design_complete = models.BooleanField(default=False)
    building_complete = models.BooleanField(default=False)
    full_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name