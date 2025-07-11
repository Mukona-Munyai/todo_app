from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('completed/<int:pk>/', views.task_completed, name='task_completed'),
]
