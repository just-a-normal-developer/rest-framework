from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class UserNames(models.Model):
    class Meta:
        verbose_name_plural = 'users'
    username = models.CharField(max_length = 200)
    email = models.EmailField()
    description = models.TextField()
    passw = models.CharField(max_length = 200 , validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.username


class Question(models.Model):
    class Meta:
        verbose_name_plural = 'questions'
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='questions')
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f' { self.user} - {self.title[:20]}'


class Answer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='answers')
    question = models.ForeignKey(Question , on_delete=models.CASCADE , related_name='qanswers')
    body = models.TextField()
    creators = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f'{self.user} - {self.question.title[:30]}'