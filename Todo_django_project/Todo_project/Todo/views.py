from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages  
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = UserCreationForm()  
    return render(request, 'todo/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = AuthenticationForm()  
    return render(request, 'todo/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('add_task')  
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

@login_required
def delete_task(request, id):
    if request.method == 'POST':
        task_to_delete = get_object_or_404(task, id=id)
        task_to_delete.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('task_list')


def task_list(request):
    tasks = task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks':tasks})