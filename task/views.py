from task.models import Task
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
# Create your views here.
def home_view(request):
    form=TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=TaskForm
        return redirect('/')
    task_list=Task.objects.all
    context={
        "form":form,
        "my_task":task_list
    }
    return render(request,"main.html",context)

def update_view(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
	    form = TaskForm(request.POST, instance=task)
	    if form.is_valid():
		    form.save()
		    return redirect('/')

    context = {'form':form}
    return render(request, 'update.html', context)


def delete_view(request,pk):
    item=Task.objects.get(id=pk)
    form=TaskForm(instance=item)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={
        'item':item
    }
    return render(request,"delete.html",context)