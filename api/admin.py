from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
#creating quiz id and title

 
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ['answer_text','is_right']
# InLine model/ TabularInLine is used to put two models on the same page to link asnwers with the question class simultaneously  

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title','quiz'] # To register a new question
    list_display = ['title','quiz','date_updated']
    inlines = [AnswerInlineModel,]
# On the qusetions page we're going to inline/add our answers using the given class

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']