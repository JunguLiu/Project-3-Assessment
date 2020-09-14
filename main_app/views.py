from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm
# Define the home view


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'


def home(request):
    tasks = Task.objects.all()
    total_time = 0
    for task in tasks:
        total_time += task.time
    form = TaskForm()
    return render(request, 'home.html', {'tasks': tasks, 'total_time': total_time, 'form': form})


def addTask(request):
    t = Task(description=request.POST.get('description'),
             time=request.POST.get('time'), person=request.POST.get('person'))
    t.save()
    return redirect('/')


def deleteTask(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')
