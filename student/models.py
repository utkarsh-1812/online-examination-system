from django.db import models

from .managers import *
# from ..teacher.models import


class Student(models.Model):
    object = StudentManager
    exams_given = models.ManyToManyField('student.exam_instance')

    def __str__(self):
        return str(self.id,)


class exam_instance(models.Model):
    exam_taker = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    exam = models.ForeignKey('teacher.Exam', on_delete=models.SET_NULL,null=True)
    date = models.TimeField(auto_now_add=True)
    marks = models.IntegerField(null=True,)
    time_taken = models.IntegerField(default=0)
    # class Meta:
    #    unique_together = (('student', 'exam','date'),)
    def __str__(self):
        return str((self.id,))


class choices(models.Model):
    ex_inst = models.ForeignKey(exam_instance, on_delete=models.CASCADE)
    ans = models.CharField(
        max_length=1,
        choices=[
            ('a', 'a'),
            ('b', 'b'),
            ('c', 'c'),
            ('d', 'd')
        ],
        null=True)
    qs = models.ForeignKey('teacher.Question', on_delete=models.SET_NULL,null=True)
    # class Meta:
    #    unique_together = (('ex_inst', 'ans','qs'),)
