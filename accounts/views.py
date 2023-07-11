from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework import status

class UserRegister(APIView):
    def post(self , request):
        ser_data = UserRegisterSerializer(data = request.POST)
        if ser_data.is_valid():
            # this is added due to say here if we do not add data then the serializer will not understand the data that should be serialized
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data , status = status.HTTP_201_CREATED)
        return Response(ser_data.errors , status= status.HTTP_400_BAD_REQUEST)