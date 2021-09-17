from django.contrib import admin

# Register your models here.
from project.models import Project, Video, Feedback, Design

admin.site.register(Video)
admin.site.register(Design)
admin.site.register(Feedback)
admin.site.register(Project)

