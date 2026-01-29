from django.shortcuts import render, redirect, get_object_or_404
from teachers.models import Teacher

# Create your views here.
def index(request):
    teachers = Teacher.objects.all()
    return render(request, 'index.html', {'data': teachers})

def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')

        Teacher.objects.create(
            first_name=first_name,
            email=email,
            subject=subject,
            phone=phone
        )
        return redirect('index')
    return render(request, 'index.html')

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.email = request.POST.get('email')
        teacher.subject = request.POST.get('subject')
        teacher.phone = request.POST.get('phone')
        teacher.save()
        return redirect('index')
    return render(request, 'index.html', {'data': Teacher.objects.all(), 'edit_teacher': teacher})

def delete_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.delete()
        return redirect('index')
    return redirect('index')