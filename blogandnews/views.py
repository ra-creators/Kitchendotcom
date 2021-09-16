from django.shortcuts import render

# Create your views here.
def blogandnews(request):
    return render(request, "blogandnews.html")

def blog(request, blogId):
    return render(request, 'blog.html')

def news(request, newsId):
    return render(request, 'news.html')