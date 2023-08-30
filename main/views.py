from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import os
from .forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse_lazy, reverse
from django.apps import apps
import uuid
User=apps.get_model('main.User_new')
Student=apps.get_model('student.Student')
Teacher=apps.get_model('teacher.Teacher')

class register_view(FormView):
    form_class = RegistrationForm
    template_name = 'registration/Registration_temp.html'
    #success_url = '/'   #hardcoded url
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        # if len(form.cleaned_data.get('query'))>10:
        #     form.add_error('query', 'Query length is not right')
        # return render(self.request, 'interface_form.html', {'form':form})
        print(form.cleaned_data)
        
        form.cleaned_data['User_ID']=uuid.uuid4().hex
        user=form.save()
        print(user.student_prof_id)

        response = super().form_valid(form)
        user=(User.objects.get(pk=form.cleaned_data.get('email')))
        #print(user.student_prof_id)
        if form.cleaned_data.get('is_student'):
            user.student_prof=Student()
            user.student_prof.save()
            print(user.student_prof.id)
        if form.cleaned_data.get('is_teacher'):
            user.teacher_prof=Teacher()
            user.teacher_prof.save()
            print(user.teacher_prof.id)
        user.save()
        return response

    '''def form_invalid(self, form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query', 'Query length is not right')
            #form.errors['__all__'] = 'Query length is not right. It should be in 10 digits.'
        response = super().form_invalid(form)
        return response'''
class LoginForm(AuthenticationForm):
    class Meta:
        model = 'main.User_new'
        fields = [
            'email',
            'Name',
            'password',
        ]
class UserLoginView(LoginView):
    template_name = "registration/Login.html"
    form_class = LoginForm
    #success_url = reverse_lazy('student:interface')

class UserLogoutView(LogoutView):
    template_name = "index.html"
    success_url = reverse_lazy('home')