from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo, Profile

from .decorators import unauth_only
from .forms import TodoForm, CreateUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def index(request):
	return render(request, 'todoer/index.html')

@unauth_only
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			Profile.objects.create(user=user)
			messages.success(request, 'Account has been created')
			return redirect('login')

	context={
			'form':form,
	}
	return render(request, 'todoer/register.html',context)


@unauth_only
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
	
		if user is not None:
			login(request, user)
			return redirect('app')
		else:
			messages.info(request, 'Invalid credentials! Try AGAIN')
	return render(request, 'todoer/login.html')


def logoutUser(request):
	logout(request)
	return redirect('index')





@login_required(login_url='login')
def app(request):
	todo_list = request.user.profile.todo_set.all()

	form = TodoForm()

	context = {'todo_list' : todo_list, 'form' : form}

	return render(request, 'todoer/app.html', context)

@require_POST
def addTodo(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.profile = request.user.profile  #assign a user profile to a task
		new_todo.save()

		return redirect('app')

def completeTodo(request, todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('app')

def deleteCompleted(request):
	Todo.objects.filter(complete__exact=True).delete()

	return redirect('app')

def deleteAll(request):
	Todo.objects.all().delete()

	return redirect('app')



