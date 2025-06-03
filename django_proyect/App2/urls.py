from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "inicio"),
    path("productos/", views.products, name = "productos"),
    path("nosotros/", views.nosotros, name = "nosotros"),
    #path("login/", views.login, name = "login"),
]