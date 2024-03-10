from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]