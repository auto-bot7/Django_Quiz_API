from rest_framework.generics import ListAPIView
from .models import Quizzes, Question
from .serializers import QuizSerializer,RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer

class RandomQuestion(APIView):
    def get(self,request, format=None,**kwargs):

        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        #quiz__title= title from quiz table,  url me se <str:title> extract kiya through kwargs, order by random , for 1 question [0:1].
        serializer = RandomQuestionSerializer(question,many=True)
        return Response(serializer.data)
        
        
class QuizQuestion(APIView): # for generating quiz on a topic dont use order_by to repeat a ques
    def get(self,request,format=None,**kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        #quiz__title= title from quiz table,  url me se <str:title> extract kiya through kwargs
        serializer = QuestionSerializer(question,many=True)
        return Response(serializer.data)   