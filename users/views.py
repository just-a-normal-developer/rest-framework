from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import UserNamesSerializer
# from django.http import HttpResponse
# Create your views here.

class Home(APIView):
    def get(self , request):
        persons = models.UserNames.objects.all()
        ser_data = UserNamesSerializer(instance= persons , many = True)
        return Response(data = ser_data.data)

    def post(self, request):
        # Logic for handling POST request
        return Response({"message": "Data received!"})
