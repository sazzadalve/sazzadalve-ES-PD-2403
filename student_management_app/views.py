from django.shortcuts import render, redirect
from . models import Student
from django.db.models import Q


# Create your views here.
def home(request):
    all_student = Student.objects.all()
    if request.method == 'GET':
        data = request.GET.get('src') 
        if data:
            all_student = Student.objects.filter(Q(name__icontains = data) | Q (roll__icontains = data))
        
    return render(request, 'index.html',{'stu': all_student})

def delete_prof(request, id):
    all_student = Student.objects.get(id=id)
    all_student.delete()
    return redirect(home)