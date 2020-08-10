from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('experience-batWomen/', views.experience, name='experience'),
    path('blog-batWomen/', views.blog_list, name='blog_list'),
]
