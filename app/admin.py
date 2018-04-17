from django.contrib import admin
#+++ Summernote +++
from django_summernote.admin import SummernoteModelAdmin
#+++ import models here. ++++
from app.models import Post , Portfolio , Resume , Project , Cert


admin.site.site_header = 'Nim4 Karimi - Django Panel :)'
#=== Post model admin ===
class PostModelAdmin(SummernoteModelAdmin):
    list_display = ['title', 'pub','draft']
    list_filter = ['pub' , 'tags']
    list_editable = ['draft']
    summernote_fields = ('body')
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
#=== Resume model admin ===
class ResumeAdmin(SummernoteModelAdmin):
    list_display = ['title','start', 'end' ]

    summernote_fields = ('body')
    class Meta:
        model = Resume

admin.site.register(Resume,ResumeAdmin)

#=== Portfolio model admin ===
class PortfolioAdmin(SummernoteModelAdmin):
    list_filter = ['pub']
    list_display = ['title']
    class Meta:
        model = Portfolio

admin.site.register(Portfolio, PortfolioAdmin)

#=== Model In Resume
admin.site.register(Project)
admin.site.register(Cert)