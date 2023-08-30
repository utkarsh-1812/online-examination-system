from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *
from django import forms
from django.core.validators import RegexValidator

class CreateQuestionsForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=5, required=True)
    
    # phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    # phone = forms.CharField(max_length=255, required=True, validators=[phone_regex])
    # query = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Question
        fields = [
            'Question',
            'Option1',
            'Option2',
            'Option3',
            'Option4',
            'Marks',
            'Answer'
        ]
class SetExamForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=5, required=True)
    
    # phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    # phone = forms.CharField(max_length=255, required=True, validators=[phone_regex])
    # query = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Exam
        fields = [
            'QP',
            'Subject',
            
        ]