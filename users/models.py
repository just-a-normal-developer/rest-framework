from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MinLengthValidator

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
