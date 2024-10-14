from django.shortcuts import render
from .models import AcademicProject

def index(request):
    academic_projects = AcademicProject.objects.all().order_by('-date_posted')
    return render(request, "index.html", {'academic_projects': academic_projects})





