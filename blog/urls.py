from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.Postlist.as_view(), name='contact'),
    path('blogpost/',views.Postlist.as_view(), name='blogpost'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), 
    
    path('',views.Postlist.as_view(), name='home'),
   
    
    #path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),    
]