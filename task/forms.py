from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
  description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10,'cols': 34}))
  deadline = forms.DateTimeField(
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
  class Meta:
    model = Task
    fields = ['title', 'description', 'image', 'complete', 'category', 'deadline']


class DeleteTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = []