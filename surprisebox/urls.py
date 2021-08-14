from django.urls import path
from .import views

urlpatterns = [
    path('userlistapi/', views.userListAPI, name="listApi"),
    path('user-list/', views.userList, name="list"),
    path('userdetailapi/<str:username>/', views.userDetailAPI, name="user"),
    path('user-detail/<str:username>/', views.userDetail, name="user"),
    path('', views.index, name="index"),
]