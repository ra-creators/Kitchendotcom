from django.contrib import admin
from home.models import c_details,kitchen_details, Constant, City1, City2, City3, City4, City5, City6, City7, City8, City9, City10

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
# admin.site.register(calculation)
admin.site.register(Constant)
admin.site.register(City1)
admin.site.register(City2)
admin.site.register(City3)
admin.site.register(City4)
admin.site.register(City5)
admin.site.register(City6)
admin.site.register(City7)
admin.site.register(City8)
admin.site.register(City9)
admin.site.register(City10)