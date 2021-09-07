from django.shortcuts import render
from .models import Post, Category


# Create your views here.


def home(request):
    # load all the Post from the database
    posts = Post.objects.all()[:11]
    categorys = Category.objects.all()
    data = {
        'posts': posts,
        'categorys': categorys,
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    categorys = Category.objects.all()
    return render(request, 'posts.html', {'post': post, 'categorys': categorys})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(category=cat)
    return render(request, 'category.html', {'cat': cat, 'posts': posts})


def about(request):
    return render(request, 'about.html')
