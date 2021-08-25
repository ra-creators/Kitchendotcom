from django.db import models

# Create your models here.
class c_details(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)

class calculation(models.Model):
    a_feet : str
    a_inch : str
    b_feet : str
    b_inch : str
    c_feet : str
    c_inch : str
    loft : str

class kitchen_details(models.Model):
    Shape : str
    Size : dict
    Material : str
    Countertop : bool
    Loft : bool
    Finish : str
    Accessories : str
    Services : dict
    Appliances : dict