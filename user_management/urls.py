from django.urls import path
from user_management import views

urlpatterns = [
    path("signUp/", views.signUp, name = "sign up"),
    path("login/", views.login, name = "login"),
    path("logout/", views.logout, name = "logout"),
    path("<str:walletAddress>/", views.user),
    path("", views.getUsers, name = "get users")
    
]