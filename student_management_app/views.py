from django.shortcuts import render, redirect
from . models import Student
from django.db.models import Q
import os


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
    if all_student.image != 'def.png':
        os.remove(all_student.image.path)
    all_student.delete()
    return redirect(home)


def create_prof(request):
    if  request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES['image']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        gender = request.POST.get('gender')
        date_of_birth = request.POST['date_of_birth']
        roll  = request.POST['roll']
        city = request.POST['city']
        is_Bangladeshi = request.POST.get('is_Bangladeshi')
        age = request.POST['age']
        #hobby = request.POST['hobby']

        student = Student(name=name, email=email, image=image, father_name=father_name, mother_name=mother_name, gender=gender, date_of_birth=date_of_birth, roll=roll, city=city, is_Bangladeshi=is_Bangladeshi, age=age)
        student.save()
        return redirect(home)

    return render(request, 'create.html')

from django.shortcuts import render, redirect
from .models import Student
import os

def update_prof(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        image = request.FILES.get('image')  # safe access
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        gender = request.POST.get('gender')
        date_of_birth = request.POST['date_of_birth']
        roll = request.POST['roll']
        city = request.POST['city']
        is_Bangladeshi = request.POST.get('is_Bangladeshi') == 'on'  # checkbox
        age = request.POST['age']

        # Only delete image if new one uploaded
        if image:
            if student.image and student.image.name != 'def.png':
                if os.path.exists(student.image.path):
                    os.remove(student.image.path)
            student.image = image  # only replace if new one uploaded

        student.name = name
        student.email = email
        student.father_name = father_name
        student.mother_name = mother_name
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.roll = roll
        student.city = city
        student.is_Bangladeshi = is_Bangladeshi
        student.age = age
        student.save()

        return redirect(home)

    return render(request, 'update.html', {'stu': student})
