from django.shortcuts import render
from .models import Student


def homeview(request):
    obj = Student.objects.all()
    return render(request,'home.html', {'obj':obj})