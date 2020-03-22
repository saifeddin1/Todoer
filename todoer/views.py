from django.shortcuts import render, redirect
from .models import Todo
from .forms import  TodoForm


def index(request):
	todo_list = Todo.objects.order_by('id')
	form = TodoForm()
	context = {'todo_list':todo_list, 'form':form}
	return render(request, 'todoer/index.html', context)


def addTask(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		
		new_task = form.save()
	
	return redirect('index')


def CompleteTask(request, task_id):
	task = Todo.objects.get(pk=task_id)
	task.complete = True
	task.save()
	return redirect('index')

def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()
	return redirect('index')
	

def deleteAll(request):
	Todo.objects.all().delete()
	return redirect('index')
	

# def editTask(request, task_id):
# 	selected = Todo.objects.get(pk=task_id)

# 	form = TodoForm(request.POST, instance=selected)

# 	if form.is_valid():
		
# 		new_task = form.save()
	
# 	return redirect('index')