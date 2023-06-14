from django.urls import path , include
from . import views

app_name = 'users'

urlpatterns = [
    path('api/' , views.Home.as_view() , name='api-test' ),

]
