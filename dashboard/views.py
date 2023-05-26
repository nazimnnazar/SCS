from django.shortcuts import render,get_list_or_404
from staff.models import *
from student.models import * 
from staff.form import TeacherForm
from django.shortcuts import render,HttpResponsePermanentRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    return render(request,'dashboard.html')

def student_details(request):
    student = StudentApplication.objects.all()
    query = request.GET.get('q')
    if query:
        student = StudentApplication.objects.filter(student_name__icontains = query) | \
                  StudentApplication.objects.filter(email__icontains=query)
    else:
        student = StudentApplication.objects.all()
    return render(request, 'das_student_details.html',{'student':student,'query':query})

def search_student():
    return render(request, '/')

def new_student(request):
    return render(request,'das_new_student.html')

def staff(request):
    staff = Teacher.objects.all()
    query = request.GET.get('q')
    if query:
        staff = Teacher.objects.filter(name__icontains = query) | \
                Teacher.objects.filter(email__icontains = query) 
    else:
        staff = Teacher.objects.all()
    return render(request,'das_staff.html',{'staff':staff,'query':query})


def staff_register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect('staff_register')
        else:
            return render(request,'staff_register.html',{'form':form})
    else:
        form =  TeacherForm()
        return render(request,'staff_register.html',{'form':form})