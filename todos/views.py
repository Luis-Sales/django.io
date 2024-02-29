from django.shortcuts import render

from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy


from .models import Todo

# Create your views here.

def todos_list(request):
    todos = Todo.objects.all
    return render(request,'todos/todo_list.html',{"todos": todos})

class TodoCreateview(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url= reverse_lazy("todo_list")
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url= reverse_lazy("todo_list")

