from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        # context = {
        #     'welcome_text':"Welcome to todo list page",
        # }
        all_tasks = TaskList.objects.all #list of objects; all object from the database
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

    #return HttpResponse("Welcome to todolist")
        
def contact(request):
    context = {
        'contact_text':"Welcome to Contact page",
    }
    #return HttpResponse("Welcome to todolist")
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text':"Welcome To About page",
    }
    #return HttpResponse("Welcome to todolist")
    return render(request, 'about.html', context)
