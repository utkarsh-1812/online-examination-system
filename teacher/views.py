from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
from django.db.models import Q
from .forms import *
from django.urls import reverse_lazy, reverse
#from .models import SellerAdditional, CustomUser, Contact, Product, ProductInCart, Cart
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

User=apps.get_model('main.User_new')
Exam=apps.get_model('teacher.Exam')
Instance=apps.get_model('student.exam_instance')
# Create your views here.
def QuestionList(Request):
    t=Question.objects.all()
    print(t)
    return HttpResponse(t)

class CreateQuestion(LoginRequiredMixin,FormView):
    form_class = CreateQuestionsForm
    template_name = 'teacher/interface_form.html'
    #success_url = '/'   #hardcoded url
    success_url = reverse_lazy('teacher:create_question')
    def form_valid(self, form):
        user=User.objects.get(pk=self.request.user.email)
        #print(self.request.user.email)
        # if len(form.cleaned_data.get('query'))>10:
        #     form.add_error('query', 'Query length is not right')
        # return render(self.request, 'interface_form.html', {'form':form})
        #print(form.save())
        user.teacher_prof.questions_created.add(form.save())
        user.teacher_prof.save()
        #print(user.teacher_prof.questions_created.all())
        response = super().form_valid(form)
        return response

    '''def form_invalid(self, form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query', 'Query length is not right')
            #form.errors['__all__'] = 'Query length is not right. It should be in 10 digits.'
        response = super().form_invalid(form)
        return response'''
class interface(LoginRequiredMixin,TemplateView):
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_teacher:
                
            #print(req.user.email,req.user.Institute_Name)
            #print(str(User.objects.get(pk=req.user.email).Institute_Name))
                return render(req, r"teacher/interface.html")
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
        #return render(req, r"index.html")
class CreateQuestionPaper(LoginRequiredMixin,TemplateView):
    template_name = 'teacher/interface_temp.html'
    #success_url = '/'   #hardcoded url
    success_url = reverse_lazy('teacher:create_question')
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_teacher:
                user=User.objects.get(pk=req.user.email)
                q_list=user.teacher_prof.questions_created.all()
                print("get",q_list)
            #print(req.user.email,req.user.Institute_Name)
            #print(str(User.objects.get(pk=req.user.email).Institute_Name))
                return render(req, r"teacher/set_qp.html",{'q_list':enumerate(q_list,start=1)})
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
    def post(self, req):
        user=User.objects.get(pk=req.user.email)
        print("post req",req.POST)
        q_list=[]
        for i in req.POST:
            if i[0]=='Q':
             print("Q",req.POST[i])
             q_list.append(
                 Question.objects.get(pk=req.POST[i])
             )   
        m=0
        qp=QuestionPaper()
        qp.save()
        for i in q_list:
            m=m+i.Marks
            qp.Questions.add(i)
            qp.save()
        qp.Full_Marks=m
        print("qp",qp.Questions.all())
        qp.save()
        #print(qp,qp.Full_Marks,qp.Questions.all())
        #user.teacher_prof.questions_created.add(form.save())
        #response = super().form_valid(form)
        return redirect(reverse_lazy('teacher:create_question_paper'))

class SetExam(LoginRequiredMixin,FormView):
    form_class = SetExamForm
    template_name = 'teacher/interface_form.html'
    #success_url = '/'   #hardcoded url
    success_url = reverse_lazy('teacher:set_exam')
    def form_valid(self, form):
        user=User.objects.get(pk=self.request.user.email)
        print(form.cleaned_data['QP'].Questions.all())
        # if len(form.cleaned_data.get('query'))>10:
        #     form.add_error('query', 'Query length is not right')
        # return render(self.request, 'interface_form.html', {'form':form})
        #print(form.save())
        user.teacher_prof.exams_created.add(form.save())
        user.teacher_prof.save()
        #print(user.teacher_prof.questions_created.all())
        response = super().form_valid(form)
        return response
    

class Result(LoginRequiredMixin,TemplateView):
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_teacher:
            #print(req.user.email,req.user.Institute_Name)
                inst_list=[]
                #print(req.POST)
                if len(req.GET)>1:
                    print(req.GET)
                    if len(req.GET['id'])>0 and len(req.GET['name'])==0:
                        print(1)
                        users=(User.objects.filter(User_ID=req.GET['id'][0]))
                    elif len(req.GET['id'])==0 and len(req.GET['name'])>0:
                        print(2)
                        users=User.objects.filter(
                            Name__icontains=req.GET['name'][0]
                            )
                    elif len(req.GET['id'])>0 and len(req.GET['name'])>0:
                        print(3)
                        users=(User.objects.filter(
                            Name__icontains=req.GET['name'][0],
                            User_ID=req.GET['id'][0])
                            )
                    else:
                        print(4)
                        users=(User.objects.all())
                    student=[]
                    
                    exam_list=(req.user.teacher_prof.exams_created.all())
                    inst_list=[]
                    for i in users:
                        student=(i.student_prof)
                        if i.is_student:
                            j=Instance.objects.filter(exam_taker=student,exam__in=exam_list)
                            if len(j)>0:
                                inst_list.append((i.Name,j))
                    #print(inst_list.order_by('exam_taker'))
                return render(req, r"teacher/result_temp.html",{'inst_list':inst_list})
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")