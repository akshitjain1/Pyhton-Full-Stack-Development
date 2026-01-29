from django.shortcuts import render
import teachers
from teachers.models import Teacher

# Create your views here.

def index(request):
    teachers = Teacher.objects.all() 
    return render(request, 'index.html', {'all_teachers': teachers})