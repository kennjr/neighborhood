from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('create-profile/', views.create_profile_page, name="create_profile_page"),
    path('neighborhoods/', views.neighborhoods_page, name="neighborhoods_page")
]