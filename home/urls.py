"""Kitchendotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path("", views.kitchen_price_steps, name='home'),
    path("select_layout", views.select_layout, name='select_layout'),
    path("customer_details", views.customer_details, name='customer_details'),
    path("select_lshape", views.lshape, name='select_lshape'), 
    path("select_ushape", views.ushape, name='select_ushape'), 
    path("select_straight", views.straight, name='select_straight'), 
    path("select_parallel", views.parallel, name='select_parallel'),
    path("select_countertop", views.select_countertop, name='select_countertop'), 
    path("select_loft_type", views.select_loft_type, name='select_loft_type'), # might be changed
    path("select_package", views.select_package, name='select_package'),
    path("select_package/premium", views.select_package_premium, name='select_package_premium'),
    path("select_package/luxe", views.select_package_luxe, name='select_package_luxe'),
    path("select_package/essentials", views.select_package_essentials, name='select_package_essentials'),
    path("select_package/buildpackage", views.select_package_buildpkg, name='select_package_buildpkg'),
    path("build_package", views.build_package, name='build_package'),
    path("build_package/hdhmr", views.build_package_hdhmr, name='build_package_hdhmr'),
    path("build_package/mrplywood", views.build_package_mrply, name='build_package_mrply'),
    path("build_package/bwrplywood", views.build_package_bwrply, name='build_package_bwrply'),
    path("build_package/bwpplywood", views.build_package_bwpply, name='build_package_bwpply'),
    
]