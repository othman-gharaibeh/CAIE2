from django.urls import path
from rest_framework import routers
from .views import PostViewSet, get_post, generate_post, summarize_post_view


router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("posts/get_post/", get_post, name="get_post"),
    path("posts/generate/", generate_post, name="generate_post"),
    path("posts/<int:post_id>/summarize/", summarize_post_view, name="summarize_post"),
]
urlpatterns += router.urls