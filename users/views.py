from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import UserNamesSerializer , QuestionSerializer , AnswerSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
# from django.http import HttpResponse
# Create your views here.
from rest_framework import status

class Home(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserNamesSerializer
    def get(self , request):

        persons = models.UserNames.objects.all()
        ser_data = UserNamesSerializer(instance= persons , many = True)
        return Response(data = ser_data.data)

    def post(self, request):
        # Logic for handling POST request
        return Response({"message": "Data received!"})

#the apiview provide the functionality to the project that inheritence come for help

class QuestionListView(APIView):
    def get(self , request):
        questions = models.Question.objects.all()
        srz_data = QuestionSerializer(instance = questions , many = True)
        return Response(srz_data.data , status= status.HTTP_200_OK )

class QuestionCreateView(APIView):
    def post(self, request):
        srz_data = QuestionSerializer(data = request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status = status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    def put(self, request , pk):
        question = models.Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance = question , data =request.data , partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data , status=status.HTTP_200_OK)
        return Response(srz_data.errors , status = status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    def delete(self, request , pk):
        question = models.Question.objects.get( pk = pk)
        question.delete()
        return Response({'message' :'deleted successfully' } , status=status.HTTP_200_OK)

