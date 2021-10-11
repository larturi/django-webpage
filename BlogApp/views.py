from django.shortcuts import render
from BlogApp.models import Post, Categoria

def blog(request):
    posts = Post.objects.all()  
    categorias = Categoria.objects.all()  
    return render(request, "BlogApp/blog.html", {'posts': posts, 'categorias': categorias})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)  
    categorias = Categoria.objects.all()  
    posts = Post.objects.filter(categorias=categoria)  

    return render(request, "BlogApp/categoria.html", {'posts': posts, 'categorias': categorias})

