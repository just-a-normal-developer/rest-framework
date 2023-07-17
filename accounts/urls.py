from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token

#here the app name added beacause when you want to use the  name space in the core url then it is needed to have  the app name in the url part of your code
#actually it is important here


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('api-token-auth/', auth_token.obtain_auth_token),
]