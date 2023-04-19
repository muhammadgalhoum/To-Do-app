from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from .forms import TaskForm, DeleteTaskForm
from .models import Task
# Create your views here.

@login_required
def home(request):
  u_i_tasks = Task.objects.filter(
      category='Urgent and important', author=request.user)
  nu_i_tasks = Task.objects.filter(
      category='Not urgent but important', author=request.user)
  u_ni_tasks = Task.objects.filter(
      category='Urgent but not important', author=request.user)
  nu_ni_tasks = Task.objects.filter(
      category='Not urgent and not important', author=request.user)
  
  context = {'u_i_tasks': u_i_tasks,'nu_i_tasks': nu_i_tasks,
            'u_ni_tasks': u_ni_tasks, 'nu_ni_tasks': nu_ni_tasks}
  return render(request, 'task/home.html', context)


@login_required
def new_task(request):
  if request.method == "POST":
    form = TaskForm(request.POST or None, request.FILES)
    if form.is_valid():
      task = form.save(commit=False)
      task.author = request.user
      task.save()
    return HttpResponseRedirect(reverse('task-detail', args=[task.id]))
  else: 
    form = TaskForm()
  
  return render(request, 'task/task_form.html', {'form': form})


@login_required
def update_task(request, pk):
  task = get_object_or_404(Task, id=pk)
  
  if task.author != request.user:
    return HttpResponse("You are not authorized to perform the update.")
  else:
    if request.method == "POST":
      form = TaskForm(request.POST, request.FILES, instance=task)
      if form.is_valid():
        form.save()
      return HttpResponseRedirect(reverse('task-detail', args=[pk]))
    else:
      form = TaskForm(instance=task)
  
  return render(request, 'task/task_form.html', {'form': form})


@login_required
def task_detail(request, pk):
  task = Task.objects.get(id=pk)
  
  if task.author != request.user:
    return HttpResponse("You are not authorized to show this page.")
  else:
    return render(request, 'task/task_detail.html', {'task': task})


@login_required
def delete_task(request,pk):
  task = get_object_or_404(Task, id=pk)
  
  if task.author != request.user:
    return HttpResponse("You are not authorized to perform the delete.")
  else:
    if request.method == "POST":
      form = DeleteTaskForm(request.POST, instance=task)
      if form.is_valid():
        task.delete()
      return HttpResponseRedirect('/')
    else:
      form = DeleteTaskForm()
  
  return render(request, 'task/delete_form.html', {'form': form, 'task': task})