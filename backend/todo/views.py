from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class = None