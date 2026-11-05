from django.db import models


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

    def __str__(self):
        author_name = self.author.username if self.author else 'Unknown'
        post_title = self.post.title if self.post else 'Unknown'
        return f"Comment by {author_name} on {post_title}"