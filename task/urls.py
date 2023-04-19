from django.urls import path
from .views import *

urlpatterns = [
  path('', home, name='home'),
  path('new_task/', new_task, name='new-task'),
  path('update_task/<str:pk>/', update_task, name='update-task'),
  path('task_detail/<str:pk>/', task_detail, name='task-detail'),
  path('delete_task/<str:pk>/', delete_task, name='delete-task'),
]