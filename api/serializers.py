from rest_framework import serializers
from .models import student,tasks

class tasksserializer(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields="__all__"

class studentserializer(serializers.ModelSerializer):
    #tasks used here because we gave that name in related _name in task model
     tasks=tasksserializer(many=True,read_only=True)
     class Meta:
         model=student
         fields="__all__"