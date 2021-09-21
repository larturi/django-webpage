from django.shortcuts import render
from BlogApp.models import Post
from BlogApp.models import Categoria

def blog(request):
    posts = Post.objects.all()  
    categorias = Categoria.objects.all()  
    return render(request, "BlogApp/blog.html", {'posts': posts, 'categorias': categorias})

