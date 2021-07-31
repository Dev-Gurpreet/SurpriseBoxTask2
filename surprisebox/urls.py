from django.urls import path
from .import views

urlpatterns = [
    path('user-list/', views.userList, name="list"),
    path('user-detail/<str:username>/', views.userDetail, name="user"),
    path('', views.index, name="index"),
]