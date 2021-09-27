from django.db import models
from rest_framework import serializers
from .models import tasksModel

class tasksSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = tasksModel 
        fields = '__all__'