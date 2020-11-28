from django.shortcuts import render, redirect
from .models import ToDo

# Create your views here.
def home(request):
    todoItems = ToDo.objects.all()

    return render(request, 'home.html', {'items': todoItems})

def addTodo(request):
    newContent = request.POST['newContent']
    new = ToDo(content = newContent)
    new.save()
    return redirect('home')

def deleteTodo(request, todo_id):
    item_to_delete = ToDo.objects.get(id = todo_id)
    item_to_delete.delete()
    return redirect('home')
