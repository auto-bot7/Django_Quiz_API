
from django.contrib import admin
from django.urls import path
from api.views import Quiz, RandomQuestion, QuizQuestion

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/',RandomQuestion.as_view(),name='random'),
    path('topic/<str:topic>/',QuizQuestion.as_view(),name='topic')
]
#use /quiz/random/Quizzes_Title(Cric quiz/G.K Quiz) to traverse not Category name
