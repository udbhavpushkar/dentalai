from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task  # Import the Celery task
import uuid

class CreateTaskView(APIView):
    def post(self, request):
        unique_task_id = str(uuid.uuid4())

        task = Task.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            status='queued',
            task_id=unique_task_id
        )

        # Trigger the Celery task
        process_task.delay(task_id=unique_task_id)

        return Response({'task_id': unique_task_id}, status=status.HTTP_201_CREATED)

class TaskStatusView(APIView):
    def get(self, request, task_id):
        try:
            task = Task.objects.get(task_id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
