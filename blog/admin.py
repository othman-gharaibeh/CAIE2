# blog/admin.py
from django.contrib import admin
from .models.user import User
from .models.post import Post
from .models.comment import Comment
from .models.category import Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'categories')
    ordering = ('-created_at',)

    # Prevents cursor overload when loading User and Category dropdowns
    raw_id_fields = ('author',)
    filter_horizontal = ('categories',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('author', 'created_at')
    raw_id_fields = ('post', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)