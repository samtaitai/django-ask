from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.new_question, name='new_question'),
    path('<int:question_id>/answers/', views.new_answer, name='new_answer'),
]