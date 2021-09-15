from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, null=False, default="Modular Kitchen")
    descriptiom = models.TextField()
    project_img = models.FileField(upload_to='projects/')
    design_complete = models.BooleanField(default=False)
    building_complete = models.BooleanField(default=False)
    full_complete = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.name