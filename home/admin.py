from django.contrib import admin
from home.models import c_details,kitchen_details,calculation

# Displaying Models
class Kd_Admin(admin.ModelAdmin):
    list_display = ["layout", "Shape", "Countertop"]


class Cd_Admin(admin.ModelAdmin):
    list_display = ["name", "phone", "email"]

class Calc_Admin(admin.ModelAdmin):
    list_display = ["a_feet", "a_inch", "b_feet", "b_inch", "c_feet", "c_inch", "loft"]


# Register your models here.
admin.site.register(c_details, Cd_Admin)
admin.site.register(kitchen_details, Kd_Admin)
admin.site.register(calculation, Calc_Admin)