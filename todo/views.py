from django.shortcuts import render, redirect
from .models import TodoModel, TasksModel
from .forms import CreateForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    context = {}
    return render(request, 'todo/index.html', context)

@login_required(login_url='/login')
def list(request, pk):
    ls = TodoModel.objects.get(id=pk)
    if ls in request.user.todolist.all():
        if request.method == 'POST':
            if request.POST.get('update_item'):
                for item in ls.tasksmodel_set.all():
                    if request.POST.get('c' + str(item.id)) == 'clicked':
                        item.done = True
                    else:
                        item.done = False
                    item.save()
            if request.POST.get('add_item'):
                txt = request.POST.get('add_text')
                if len(txt) > 2:
                    ls.tasksmodel_set.create(text=txt, done=False)
                else:
                    print('Invalid')
        return render(request, 'todo/list.html', {'ls': ls})
    context = {'ls': ls}
    return render(request, 'todo/list.html', context)

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = TodoModel(name=n)
            t.save()
            request.user.todolist.add(t)
        return redirect('/%i' %t.id)
    else:
        form = CreateForm()
    context = {'form': form}
    return render(request, 'todo/create.html', context)

@login_required(login_url='/login')
def view_list(request):
    return render(request, 'todo/view_list.html', {})




