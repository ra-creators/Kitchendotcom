from django.shortcuts import get_object_or_404, render
from project.models import Project, PostImage

# Create your views here.
def projectList(request):
    projects = Project.objects.all()
    for project in projects:
        print(project)
    return render( request, "project_gallery.html", {project:projects})

# def projectDetails(request, projectId):
#     try:
#         context = {}
#         __project = Project.objects.get(id=projectId)
#         # __project = Project.objects.filter(Project=__project)
#         context = {'project': __project}
#     # __project = 
#         print(__project)
#         return render( request, "project_details.html", context)
#     except:
#         print("not found")
#         return render( request, "project_details.html")

# Newly added
def projectList(request):
    posts = Project.objects.all()
    return render(request, 'project_gallery.html', {'posts':posts})
 
def projectDetails(request, id):
    post = get_object_or_404(Project, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'project_details.html', {
        'post':post,
        'photos':photos
    })