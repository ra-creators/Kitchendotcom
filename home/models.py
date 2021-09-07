from django.db import models

# Create your models here.
class c_details(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)

    def __str__(self):
        return self.name


class kitchen_details(models.Model):

    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    
    def __str__(self):
        return self.Name

# Model after adding sessions
class Constants(models.Model):
    essentials = models.CharField(max_length=12, default="NA")
    premium = models.CharField(max_length=12, default="NA")
    luxe = models.CharField(max_length=12, default="NA")
    countertop = models.CharField(max_length=12, default="NA")