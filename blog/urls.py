from blog.models import ControlFlow
from django.urls import path
from .views import ControlFlowView, PostListView, PostDetailView, ReplyCommentView,ProfileView, ProfileEditView,AboutMe,SearchView,AddLike,DisLike, TableOfContent, BasicView

urlpatterns = [
    path('post/<int:post_pk>/comment/<int:pk>/reply', ReplyCommentView.as_view(), name='comment-reply'),
    path('contact/',PostListView.as_view(), name='contact'),
    path('blogpost/',PostListView.as_view(), name='blogpost'), 
    path('about_me/', AboutMe.as_view(), name='about-me'),
    path('post_search/', SearchView.as_view(), name='search-post'), 
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'), 
    path('profile/<int:pk>',ProfileView.as_view(), name='profile' ),
    path('profile/edit/<int:pk>/',ProfileEditView.as_view(), name='profile-edit' ),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'), 
    path('post/<int:pk>/dislike', DisLike.as_view(), name='dislike'), 
    
    path('python_table_of_content/', TableOfContent.as_view(), name='python-content'),
    path('basics_of_programming_in_python/', BasicView.as_view(), name='python-basics'),
    path('control_flow_tools_in_python/', ControlFlowView.as_view(), name='control-flow'),
   
    path('',PostListView.as_view(), name='home'),
    
   
    
    #path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),    
]