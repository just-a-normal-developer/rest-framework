from rest_framework import serializers
from .models import UserNames , Question , Answer

class UserNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNames
        fields = ['id', 'username', 'email', 'description', 'passw']

class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

    def get_answer(self , object):
        result = object.qanswers.all()
        return AnswerSerializer(instance = result , many = True).data

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
