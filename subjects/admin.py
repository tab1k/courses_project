from django.contrib import admin

from subjects.models import *

# Register your models here.

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    pass

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass