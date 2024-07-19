from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myspace/', views.MySpace, name='myspace'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]