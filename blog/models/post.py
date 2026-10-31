from django.db import models

from models import User
from models import Category

class Post(models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)

    def __str__(self):
        return self.title