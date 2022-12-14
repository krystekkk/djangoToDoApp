from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('edit/<str:pk>', views.edit, name="edit"),
    path('register/', views.register, name="register"),
]
