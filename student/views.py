from django.shortcuts import render
from django.shortcuts import render,HttpResponsePermanentRedirect
from . models import *
from .form import StudentApplicationForm

def student_register(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('/')
        else:
            return render(request,'application.html',{'form':form})
    else:
        form = StudentApplicationForm()
        return render(request,'application.html',{'form':form})
