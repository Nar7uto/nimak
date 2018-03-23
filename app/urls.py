from django.urls import path , include

# +++ Import Custom Views +++
from app.views import PostDetailView, PostListView , index


urlpatterns = [
    path('',index , name ='home'),
    # Post
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostDetailView.as_view() , name ='post-detail'),

]

