from django.contrib import admin
from django.db import models
from home.models import c_details, kitchen_details, Constant, City1, City2, City3, City4, City5, City6, City7, City8, City9, City10, TempLink
from datetime import date, datetime, timedelta

# Displaying Models
# class Kd_Admin(admin.ModelAdmin):
#     list_display = ["layout", "Shape", "Countertop", "loft"]


# class Cd_Admin(admin.ModelAdmin):
#     list_display = ["name", "phone", "email"]

# class Calc_Admin(admin.ModelAdmin):
#     list_display = ["a_feet", "a_inch", "b_feet", "b_inch", "c_feet", "c_inch"]


# Register your models here.
admin.site.register(c_details)
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


@admin.action(description="Create temp links")
def create_link(modeladmin, request, queryset):
    for query in queryset:
        TempLink.objects.create(kitchen_details=query)


@admin.register(kitchen_details)
class kitchen_detailsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Location', 'Price', 'getTempLink',  'link_expiry']
    # ordering = ['Date']

    def getTempLink(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x)
        return tempLinkObj.link

    def link_expiry(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x)
        if tempLinkObj.date:
            date_diff = (datetime.now().date() - tempLinkObj.date)
            if(date_diff.days > 2):
                return 'expired'
            else:
                return (tempLinkObj.date + timedelta(days=2))
        else:
            return '-'

    actions = [create_link]

    class Media:
        js = ("admin/copy-btn.js",)


@admin.register(TempLink)
class TempLinkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'getTempLink', 'expiry_date']

    def getTempLink(self, x):
        return x.link

    def expiry_date(self, x):
        return (x.date + timedelta(days=2))

    class Media:
        js = ("admin/copy-btn.js",)
