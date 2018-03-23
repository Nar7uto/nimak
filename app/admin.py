from django.contrib import admin

#+++ import models here. ++++
from app.models import Post

#=== Post model admin ===

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub']
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)

