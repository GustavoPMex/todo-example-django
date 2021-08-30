from rest_framework import viewsets
from .models import tasksModel
from .serializer import tasksSerializer

class tasksViewSet(viewsets.ModelViewSet):
    queryset = tasksModel.objects.all()
    serializer_class = tasksSerializer