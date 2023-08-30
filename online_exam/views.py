from django.http import HttpResponse, FileResponse
from django.shortcuts import render
import os
#from ..main.forms import *
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View

def home(request):
    return render(request, r"index.html")
    
    # if file:
    #     return render(request, r"Home/"+file)
    # else:
    #     return render(request, r"Home/index.html")
    


def css(request, file):
    print("css", file)
    return HttpResponse(request, file)  # +".css")\


def image(request, file):
    #print(request.GET)
    print("image", file)
    print(os.getcwd())
    img = open('templates/images/'+file, 'rb')
    #img = open('C:/Users/student/Desktop/Python/online_exam/online_exam/templates/images/'+file, 'rb')

    response = FileResponse(img)
    return response
# def invalid(request,url):
#    print
# C:/Users/student/Desktop/Python/online_exam/online_exam/templates/

def contact(req):
    return render(req,r"contact.html")
def about(req):
    return render(req,r"about.html")
