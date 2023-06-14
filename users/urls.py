from django.urls import path , include
from . import views


urlpatterns = [
    path('api/' , views.Home.as_view() , name='testing' ),

]
