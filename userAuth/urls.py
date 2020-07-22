# accounts/urls.py
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
