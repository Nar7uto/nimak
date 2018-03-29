from django.urls import path , include , re_path
from django.views.static import serve
from django.conf import settings
# from django.views.generic.dates import ArchiveIndexView
from .views import PostYearArchiveView

# +++ import model +++
from .models import Post
# +++ Import Custom Views +++
from app.views import (
    PostDetailView,
    PostListView ,
    index ,
    portfolio ,
    resume,
    contact,
    TagPostView,
)


urlpatterns = [
    # Index View
    path('',index , name ='home'),

    # Post
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/tags/<slug:slug>', TagPostView.as_view(), name='tagged'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name = 'post-detail'),
    # path('posts/archive/', ArchiveIndexView.as_view(model=Post, date_field='pub', name='posts-archive')),
    path('posts/archive/<int:year>/',PostYearArchiveView.as_view(),name="post_year_archive"),
    # Resume
    path('resume/', resume , name='resume'),
    # Portfolio
    path('portfolio/', portfolio , name='portfolio'),
    # Contact
    path('contact/', contact , name ='contact'),
    # Summernote
    re_path(r'^summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]