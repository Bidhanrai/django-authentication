from rest_framework import viewsets
from blog.models import Post, Comment
from django.contrib.auth.models import User
from blog.serializers import PostSerializer, CommentSerializer
from userAuth.serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
