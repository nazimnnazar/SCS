from django.contrib import admin
from .models import *

@admin.register(StudentApplication)
class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = StudentApplication.DisplayFields
    search_fields = StudentApplication.SearchableFields