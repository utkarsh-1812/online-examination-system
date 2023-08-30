from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.


class Database_Error(object):
    def __init__(self, arg):
        self._arg = arg

    def __call__(self, *args, **kwargs):
        val = self._arg(*args, **kwargs)
        print('called')
        return val


class Q_manage(models.Manager):
    @Database_Error
    def all(self):
        q = self.all()
        print('1')
        return ['hi']


class Question(models.Model):
    #Q_ID = models.IntegerField(unique=True, primary_key=True,auto_created=True)
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=30)
    Option2 = models.CharField(max_length=30)
    Option3 = models.CharField(max_length=30)
    Option4 = models.CharField(max_length=30)
    Marks = models.IntegerField(default=0)
    Answer = models.CharField(
        max_length=1,
        choices=[
            ('a', Option1),
            ('b', Option2),
            ('c', Option3),
            ('d', Option4)
        ],
        null=True)

    objects = Q_manage

    @classmethod
    def modify_opt(cls, id, opt, new):
        Q = cls.objects.get(Q_ID=id)
        if opt == 'a':
            Q.Option1 = new
        elif opt == 'b':
            Q.Option2 = new
        elif opt == 'c':
            Q.Option3 = new
        elif opt == 'd':
            Q.Option4 = new
        else:
            raise Exception(
                "Invalid value for opt, allowed values =(a,b,c,d) ")
        Q.save()

    @classmethod
    def modify_qs(cls, id, new):
        Q = cls.objects.get(Q_ID=id)
        Q.Question = new
        Q.save()

    @classmethod
    def modify_ans(cls, id, new):
        Q = cls.objects.get(Q_ID=id)
        Q.Answer = new
        Q.save()

class QuestionPaper(models.Model):
    #Qp_ID = models.IntegerField(unique=True, primary_key=True)
    Questions = models.ManyToManyField(Question)
    created = models.DateTimeField(default=timezone.now,null=True)
    Full_Marks = models.IntegerField(default=0)
    Time_limit = models.IntegerField(default=0)


class Exam(models.Model):
    #Ex_ID = models.IntegerField(unique=True, primary_key=True)
    Subject=models.CharField(max_length=100,null=True,default='Computer Science')
    QP = models.ForeignKey(QuestionPaper, on_delete=models.SET_NULL,null=True)
    due_date = models.TimeField(null=True, blank=True)
    def __str__(self):
        return str((self.id,self.created))
    
class Teacher(models.Model):
    questions_created = models.ManyToManyField(Question)
    qp_created = models.ManyToManyField(QuestionPaper)
    exams_created = models.ManyToManyField(Exam)
    manages=models.ManyToManyField('teacher.Class')
    #user_prof=models.ForeignKey('student.Student')
    def __str__(self):
        return (self.id,)




class Class(models.Model):
    course= models.CharField(max_length=255, blank=True, null=True)
    incharge= models.ManyToManyField(Teacher)
    students= models.ManyToManyField('student.Student')
