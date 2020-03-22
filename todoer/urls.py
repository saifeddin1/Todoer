from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('add', addTask, name="add"),
    path('complete/<task_id>', CompleteTask, name="complete"),
    path('delete_completed', deleteCompleted, name="delete_completed"),
    path('delete_all', deleteAll, name="delete_all"),
    # path('edit/<task_id>', editTask, name="edit"),
]
