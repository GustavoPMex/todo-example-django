from .models import tasksModel
from .serializer import tasksSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

class taskList(generics.ListCreateAPIView):
    serializer_class = tasksSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        # User tasks
        return tasksModel.objects.filter(owner=user)

class EditTask(generics.UpdateAPIView):
    queryset = tasksModel
    serializer_class = tasksSerializer
    permission_classes = (IsAuthenticated, )


class DeleteTask(generics.DestroyAPIView):
    queryset = tasksModel 
    serializer_class = tasksSerializer
    permission_classes = (IsAuthenticated, )