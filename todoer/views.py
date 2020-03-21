from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
	tasks = Task.objects.order_by('id')
	form = TaskForm()
	context = {'tasks':tasks, 'form':form}
	return render(request, 'todoer/index.html', context)


def addTask(request):
	form = TaskForm(request.POST)
	if form.is_valid():
		new_task = Task(name=request.POST['name'])
		new_task.save()
	return redirect('index')


def CompleteTask(request, task_id):
	task = Task.objects.get(pk=task_id)
	task.complete = True
	task.save()
	return redirect('index')

def deleteCompleted(request):
	Task.objects.filter(complete__exact=True).delete()
	return redirect('index')
	

def deleteAll(request):
	Task.objects.all().delete()
	return redirect('index')
	