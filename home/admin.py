from django.contrib import admin
from home.models import c_details,kitchen_details,calculation

# Displaying Models
# class Kd_Admin(admin.ModelAdmin):
#     list_display = ["layout", "Shape", "Countertop", "loft"]


# class Cd_Admin(admin.ModelAdmin):
#     list_display = ["name", "phone", "email"]

# class Calc_Admin(admin.ModelAdmin):
#     list_display = ["a_feet", "a_inch", "b_feet", "b_inch", "c_feet", "c_inch"]


# Register your models here.
admin.site.register(c_details)
admin.site.register(kitchen_details)
admin.site.register(calculation)