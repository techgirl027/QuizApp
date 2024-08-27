from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.home_page, name="index"),
    path("login/", views.login_, name="login"),
    path("register/", views.register, name="register"),
]
