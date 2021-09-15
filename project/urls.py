from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectList, name="projectList"),
    path('<int:projectId>', views.projectDetails, name="projectDetails"),
]