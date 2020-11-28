from django.urls import path, include
from task import views

urlpatterns = [
     path('', views.home, name='home'),
     path('addTodo/', views.addTodo, name='addTodo'),
     path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='delete'),
]
