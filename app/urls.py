from django.urls import path , include

# +++ Import Custom Views +++
from app.views import (
    PostDetailView,
    PostListView ,
    index ,
    portfolio ,
    resume
)


urlpatterns = [
    # Index View
    path('',index , name ='home'),

    # Post
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostDetailView.as_view() , name ='post-detail'),
    # Resume
    path('resume/', resume , name='resume'),
    # Portfolio
    path('portfolio/', portfolio , name='portfolio'),
]

