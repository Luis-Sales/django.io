
from django.contrib import admin
from django.urls import path

from todos.views import todos_list, TodoCreateview,TodoUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  todos_list, name="todo_list"),
    path('create', TodoCreateview.as_view(), name="todo_create" ),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update" )
    
    
    ]
