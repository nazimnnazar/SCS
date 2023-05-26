from django.contrib import admin
from . models import *

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = Teacher.DisplayFields
    search_fields = Teacher.SearchableFields