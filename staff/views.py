from django.shortcuts import render
from django.shortcuts import render,HttpResponsePermanentRedirect
from . models import *
from .form import TeacherForm

def teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('/')
        else:
            return render(request,'teacher.html',{'form':form})
    else:
        form = TeacherForm()
        return render(request,'teacher.html',{'form':form})