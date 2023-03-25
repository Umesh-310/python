from django.shortcuts import render
from .models import Students
# Create your views here.


def list_student(request):
    all_student = Students.objects.all()
    context = {'student': all_student}
    return render(request, 'insert_app/list.html', context=context)
