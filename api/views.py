print("view loaded")
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet #remember M and V and S are in capital
from .models import student,tasks
from .serializers import tasksserializer,studentserializer 

class studentviewset(ModelViewSet):#studentviewset inherit all the power of Modelviewset
    queryset=student.objects.all()#to get all the data from student database #data on which this API should work
    serializer_class=studentserializer #it tells API use this serializer to convertdata between python objects to JASON


class tasksviewset(ModelViewSet):
    queryset=tasks.objects.all()
    serializer_class=tasksserializer


