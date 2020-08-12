from .viewsets import PostViewSet, UserViewSet, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', PostViewSet)
router.register('user', UserViewSet)
router.register('comment', CommentViewSet)