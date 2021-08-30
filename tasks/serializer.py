from django.db import models
from rest_framework import serializers
from .models import tasksModel

class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasksModel
        fields = '__all__'