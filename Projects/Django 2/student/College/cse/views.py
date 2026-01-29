from django.shortcuts import render
from cse.models import Student
# Create your views here.
def index(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'info': data})
