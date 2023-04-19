from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .decorators import unauthenticated
# Create your views here.


@unauthenticated
def register(request):
  if request.method == "POST":
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
    username = form.cleaned_data.get('username')
    messages.success(request, f"Account was created for {username}  successfully!")
    return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'accounts/register.html', {'form': form})


@unauthenticated
def login_form(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.info(request, 'Username or Password is Incorrect!')
  return render(request, 'accounts/login.html', {})


@login_required
def logout_user(request):
  logout(request)
  return redirect('home')


@login_required
def delete_account(request, uid):
  user = get_object_or_404(User, id=uid)
  if request.method == "POST":
    form = UserDeleteForm(request.POST, instance=user)
    user.delete()
    messages.success(request, ('Your account has been deleted successfully.'))
    return redirect('home')
  else:
    form = UserDeleteForm(instance=user)
  return render(request, 'accounts/delete_account.html', {'form': form})


@login_required
def profile(request):
  if request.method == "POST":
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
    
    messages.success(request, "Account has been updated successfully!")
    return redirect('profile')
  else:
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
  return render(request, 'accounts/profile.html', {'user_form': user_form, 'profile_form': profile_form})