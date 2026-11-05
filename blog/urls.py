from django.urls import path
from rest_framework import routers
from .views import PostViewSet, get_post

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('posts/get_post/', get_post, name='get_post' ),
]
urlpatterns += router.urls