from django.forms import ModelForm
from django import forms
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'duedate', 'urgent']