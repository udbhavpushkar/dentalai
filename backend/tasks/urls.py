from django.urls import path
from .views import CreateTaskView, TaskStatusView

urlpatterns = [
    path('tasks/', CreateTaskView.as_view(), name='create_task'),
    path('tasks/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]
