from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title',]
    


class AnswerSerializer(serializers.ModelSerializer):
            class Meta:
                model = Answer
                fields = ['id','is_right','answer_text']


class RandomQuestionSerializer(serializers.ModelSerializer):
    #answer = serializers.StringRelatedField(many=True) # using this will return answers object values eg.(answer object (19)) to get answers return __str__ answer.answer text from models
    quiz = QuizSerializer(read_only=True) #displays quiz title on top quiz{ques{answers}}
    answer = AnswerSerializer(many=True, read_only=True) #nested serializers
    class Meta:
        model = Question
        fields = ['quiz','title','answer'] #this will only generate keys for answers


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True) #displays quiz title on top quiz{ques{answers}}
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['quiz','title','answer'] #this will only generate keys for answers