from django.shortcuts import get_object_or_404, render
from .models import Blog, News, BlogComment
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
    comments = BlogComment.objects.filter(blog=blog)
    context = {'blog' : blog, 'comments' : comments} 
    return render(request, 'blog.html', context)

def blogComment(request, blogId):
    if request.method == "POST":
        comment = request.POST.get("comment")
        name = request.POST.get("name")
        email = request.POST.get("email")
        blogSno = request.POST.get("blogSno")
        blog = Blog.objects.get(sno=blogSno)
        
        comment = BlogComment(comment = comment, name=name, email=email, blog=blog)
        comment.save()    
    
    return render("/blog") # to be changed