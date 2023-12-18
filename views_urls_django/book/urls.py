from django.urls import path 
from .views import *

urlpatterns = [
    path('get/', my_book),
    path('create/', create_book),
    path('get/<int:pk>/', get_one_book),
    path('update/<int:pk>/', update_book),
    path('delete/<int:pk>/', delete_book),
    path('patch_update/<int:pk>/', patch_update_book)
]