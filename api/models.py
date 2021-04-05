from django.db import models
from django.utils.translation import gettext_lazy as _ #for translation

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")   #alias name for model when they are too complex ex Itemforsale(models.Model): verbose_name= _("Item for sale")
        verbose_name_plural = _("Quizzes") #django defaults to add an 's' to make it plural verbose_name_plural = _("items_for_sale")
        ordering = ['id']

    title=models.CharField(max_length=255, default = _("New Quiz"), verbose_name = _("Quiz TItle"))
    #default=defaultvalue for a new entry
    
    category=models.ForeignKey(Category,default=1, on_delete=models.DO_NOTHING)
    #default=1 when we add a new quiz it's going to have whatever the 1st category we have in category table 
    
    date_created = models.DateTimeField(auto_now_add= True)
    #When this model is created a date is generated if we use auto_now date of updation is stored

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))
    
    class Meta:
        abstract = True


class Question(Updated):
    
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (0, _('Expert')),
    )
    # an option for user to select difficulty level
    TYPE = (
        (0, _('Multiple Choice')),
    )
    
    # Option to select type of questions

    quiz = models.ForeignKey(Quizzes,related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices = TYPE, default = 0, verbose_name =  _("Type of Question"))
    #choices - provides a dropdown option ,  default = 0 - by def. option 0 is selected
    title = models.CharField(max_length=255, verbose_name= _("Title"))
    difficulty = models.IntegerField(choices = SCALE, default = 0, verbose_name =  _("Difficulty"))
    date_created = models.DateTimeField(auto_now_add= True, verbose_name= _("Date Created"))
    is_active = models.BooleanField(default= False, verbose_name= _("Active Status"))

    def __str__(self):
         return self.title
     

class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    #this class contains answer_text field for storing answers, and is_right is to associate a boolean valur T/F for the answer.
    
    question = models.ForeignKey(Question,related_name='answer', on_delete=models.DO_NOTHING)
    # This field is going to have question and question id 
    answer_text = models.CharField(verbose_name = _("Answer Text"), max_length=50)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    