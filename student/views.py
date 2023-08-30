from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.apps import apps

User=apps.get_model('main.User_new')
Exam=apps.get_model('teacher.Exam')
instance=apps.get_model('student.exam_instance')
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

# Create your views here.

# def interface(req):
#     return render(req, r"interface.html")

class interface(LoginRequiredMixin,TemplateView):
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_student:
            #print(req.user.email,req.user.Institute_Name)
            #print(str(User.objects.get(pk=req.user.email).Institute_Name))
                return render(req, r"student/interface.html")
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
        #return render(req, r"index.html")

class Result(LoginRequiredMixin,TemplateView):
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_student:
            #print(req.user.email,req.user.Institute_Name)
                user=(User.objects.get(pk=req.user.email))
                exam_list=(user.student_prof.exams_given.all())
                return render(req, r"student/result_temp.html",{'exam_list':exam_list})
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
class ChooseExam(LoginRequiredMixin,TemplateView):
    def get(self,req):
        if req.user.is_authenticated:
            if req.user.is_student:
            #print(req.user.email,req.user.Institute_Name)
                #user=(User.objects.get(pk=req.user.email))
                exam_list=(Exam.objects.all())
                return render(req, r"student/interface_temp.html",{'exam_list':exam_list})
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
class exam(LoginRequiredMixin,TemplateView):
    inst=None
    q_list=None
    def get(self,req,**kwargs):
        if req.user.is_authenticated:
            if req.user.is_student:
            #print(req.user.email,req.user.Institute_Name)
                self.user=(User.objects.get(pk=req.user.email))
                self.inst=instance(
                    exam_taker=self.user.student_prof,
                    exam=Exam.objects.get(pk=kwargs['exam'])
                    )
                
                self.q_list=Exam.objects.get(pk=kwargs['exam']).QP.Questions.all()
                print(Exam.objects.get(pk=kwargs['exam']).QP.Questions.all())
                return render(req, r"student/questions.html",{'q_list':enumerate(self.q_list,start=1)})
            else:
                return render(req,r"index_form.html",{'message':'You Do Not Have Required Permission'})
        else:
            return redirect(f"{settings.LOGIN_URL}?next={req.path}")
    def post(self,req,exam):
        print(req.POST)
        self.user=(User.objects.get(pk=req.user.email))
        self.inst=instance(
                exam_taker=self.user.student_prof,
                exam=Exam.objects.get(pk=exam)
                )
                
        self.q_list=self.inst.exam.QP.Questions.all()
        m=0
        for i in req.POST:
            if i[0]=='Q':
                if(self.q_list[int(i[1])-1].Answer==req.POST.get(i)):
                    m=m+self.q_list[int(i[1])-1].Marks
                #print(self.q_list[int(i[1])-1].Answer,req.POST.get(i))
        self.inst.marks=m
        self.inst.save()
        self.user.student_prof.exams_given.add(self.inst)
        self.user.student_prof.save()  
        return render(req,r"index_form.html",{'message':f'Exam Submitted Successfully, Marks Obtained: {m}/{self.inst.exam.QP.Full_Marks}'}) 
