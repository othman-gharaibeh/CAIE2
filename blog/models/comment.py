from django.db import models
from models import User
from models import post



class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(post.Post, on_delete=models.CASCADE, related_name='comments', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', blank=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"