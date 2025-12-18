from django.contrib import admin

# Register your models here.

from .models import *

# admin.site.register(Student)
# admin.site.register(SubStudent)

@admin.register(Student)
class PracticeTestQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email')
    list_filter = ('name', 'email')
    search_fields = ('name','email')

@admin.register(SubStudent)
class PPracticeTestQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub','title','address')
    list_filter = ('id','sub','title', 'address')
    search_fields = ('title','address')