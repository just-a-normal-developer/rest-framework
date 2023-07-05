from django.urls import path , include
from . import views

app_name = 'users'

urlpatterns = [
    path('api/' , views.Home.as_view() , name='api-test' ),
    path('questions/', views.QuestionListView.as_view(), name='question_list'),
    path('questions/create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('questions/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='question_update'),
    path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view(), name='question_delete'),

]
