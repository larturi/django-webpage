from django.shortcuts import render
from BlogApp.models import Post

def blog(request):
    posts = Post.objects.all()  
    return render(request, "BlogApp/blog.html", {'posts': posts})

