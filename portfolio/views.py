from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from .signals import request_date_signal
# Create your views here.


def home(request):
    request_date_signal.send(sender=Post, date='2020-12-3')
    return render(request, 'portfolio/home.html', {})


def about(request):
    return render(request, 'portfolio/about.html', {})


def experience(request):
    return render(request, 'portfolio/experience.html', {})


def blog_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/blog_list.html', {'posts': posts})


