from multiprocessing import context
from django.shortcuts import render,HttpResponse
import datetime



# Create your views here.
def index(request):

 return render(request,'index.html')


def about(request):
    return render(request,'about.html')   

def contact(request):
    return render(request,'contact.html')


def feature(request):
    return render(request,'feature.html')

def project(request):
    return render(request,'project.html')

def testimonial(request):
    return render(request,'testimonial.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')