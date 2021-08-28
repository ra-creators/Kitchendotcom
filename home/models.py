from django.db import models

# Create your models here.
class c_details(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)

    def __str__(self):
        return self.name

class calculation(models.Model):
    a_feet = models.CharField(max_length=3, default="0")
    a_inch = models.CharField(max_length=3, default="0")
    b_feet = models.CharField(max_length=3, default="0")
    b_inch = models.CharField(max_length=3, default="0")
    c_feet = models.CharField(max_length=3, default="0")
    c_inch = models.CharField(max_length=3, default="0")
    loft = models.CharField(max_length=12, default="0")
    

class kitchen_details(models.Model):
    layout = models.CharField(max_length=30, default="0")
    Shape = models.CharField(max_length=12, default="0")
    Size : dict
    Material = models.CharField(max_length=12, default="0")
    Countertop = models.CharField(max_length=12, default="0")
    Loft = models.CharField(max_length=12, default="0")
    Finish = models.CharField(max_length=12, default="0")
    Accessories = models.CharField(max_length=12, default="0")
    Services : dict
    Appliances : dict
    customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    cal = models.ForeignKey(calculation, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.layout