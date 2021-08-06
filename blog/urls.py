from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('',views.Postlist.as_view(), name='home'),
    
    #path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),    
]