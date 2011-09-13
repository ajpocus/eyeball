from django.template import RequestContext
from django.shortcuts import render, redirect

from tasks.models import Task
from tasks.forms import TaskAddForm

def tasks_list(request):
    tasks = Task.objects.filter(is_finished=False)
    c = RequestContext(request, {
	'tasks': tasks,
    })
    return render(request, 'tasks/tasks_list.html', context_instance=c)

def tasks_add(request):
    if request.method == 'POST':
	form = TaskAddForm(request.POST)
	if form.is_valid():
	    form.process()
	    return redirect('/tasks/')
    else:
	form = TaskAddForm()

    c = RequestContext(request, {
	'form': form,
    })

    return render(request, 'tasks/task_add.html', context_instance=c)

