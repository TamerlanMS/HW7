from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'detail.html', {'todo': todo})

def create_or_update_todo(request, todo_id=None):
    if todo_id:
        todo = get_object_or_404(Todo, id=todo_id)
    else:
        todo = None

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')

        if todo:
            todo.title = title
            todo.body = body
            todo.deadline = deadline
            todo.status = status
        else:
            todo = Todo.objects.create(title=title, body=body, deadline=deadline, status=status)
        
        todo.save()
        messages.success(request, 'Todo saved successfully.')
        return redirect('home')

    return render(request, 'create_or_update_todo.html', {'todo': todo})
