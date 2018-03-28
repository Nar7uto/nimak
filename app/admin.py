from django.contrib import admin
#+++ Summernote +++
from django_summernote.admin import SummernoteModelAdmin
#+++ import models here. ++++
from app.models import Post

#=== Post model admin ===

class PostModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'pub']
    summernote_fields = ('body')
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)


