from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('create-client/', views.create_client, name='createclient'),
    path('view/<int:client_id>', views.view_client, name='view_client'),
    path('update/<int:client_id>', views.update_client, name='update_client'),
    path('delete/<int:client_id>', views.delete_client, name='delete_client'),
    path('search/', views.search_clients, name='search_clients'),
    path('create_category/', views.create_category, name='create_category')
]