from django.urls import path
from .  import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('student_details',views.student_details,name='student_details'),
    path('new_student',views.new_student,name='new_student'),
    path('staff',views.staff,name='staff'),
    path('staff_register',views.staff_register,name='staff_register'),
    path('search_student',views.search_student,name = 'search_student'),
]