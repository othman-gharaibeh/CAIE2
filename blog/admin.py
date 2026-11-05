
from django.contrib import admin

from .models.user import User
from .models.post import Post
from .models.comment import Comment
from .models.category import Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'title_id')
    search_fields = ('title', 'content')
    list_filter = ('author',)
    ordering = ('-title_id',)  


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('content',)
    list_filter = ('author', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)