from django.urls import path
from .views import PostListView, PostDetailView, ReplyCommentView

urlpatterns = [
    path('post/<int:post_pk>/comment/<int:pk>/reply', ReplyCommentView.as_view(), name='comment-reply'),
    path('contact/',PostListView.as_view(), name='contact'),
    path('blogpost/',PostListView.as_view(), name='blogpost'),  
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'), 
   
    path('',PostListView.as_view(), name='home'),
    
   
    
    #path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),    
]