from django.urls import path , include , re_path
from django.views.static import serve
from django.conf import settings

# +++ Import Custom Views +++
from app.views import (
    PostDetailView,
    PostListView ,
    index ,
    portfolio ,
    resume,
    TagPostView,
)


urlpatterns = [
    # Index View
    path('',index , name ='home'),

    # Post
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/tag/<slug:slug>', TagPostView.as_view(), name='tagged'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name = 'post-detail'),

    # Resume
    path('resume/', resume , name='resume'),
    # Portfolio
    path('portfolio/', portfolio , name='portfolio'),

    # Summernote
    re_path(r'^summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]