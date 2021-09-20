from django.shortcuts import get_object_or_404, render
from .models import Blog, News
# Create your views here.
def blogandnews(request):
    blogs = Blog.objects.all() 
    newss = News.objects.all() 
    return render(request, "blogandnews.html",{
        'blogs':blogs,
        'newss':newss,
    })

def blog(request, blogId):
    blog = get_object_or_404(Blog, id=blogId)
    return render(request, 'blog.html', {'blog':blog})