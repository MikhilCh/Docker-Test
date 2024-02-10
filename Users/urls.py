from django.urls import path
from .views import hello_world, register, get_user_by_id, get_user_details

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('add_user/', register, name='register'),
    path('get_user/<int:user_id>/', get_user_by_id, name='user by id'),
    path('get_user_details', get_user_details, name='user details'),
]