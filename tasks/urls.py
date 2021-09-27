from django.urls import path
from .apiviews import taskList, EditTask, DeleteTask


urlpatterns = [
    path('v1/tasks/', taskList.as_view(), name='list'),
    path('v1/tasks/edit/<int:pk>/', EditTask.as_view(), name='edit_task'),
    path('v1/tasks/delete/<int:pk>/', DeleteTask.as_view(), name='delete_task')

]