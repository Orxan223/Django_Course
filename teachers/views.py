from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Teacher
# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name= 'teachers'
