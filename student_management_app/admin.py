from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','roll', 'age', 'image']
    search_fields = ['name','roll', 'age', 'father_name', 'mother_name']


admin.site.register(Student, StudentAdmin)
admin.site.register(Hobby)
admin.site.register(Subject)
admin.site.register(Result)