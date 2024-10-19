from django.shortcuts import render
from .models import AcademicProject

def index(request):
    academic_projects = AcademicProject.objects.all()
    return render(request, 'index.html', {'academic_projects': academic_projects})




