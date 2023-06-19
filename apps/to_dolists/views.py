from django.shortcuts import render, redirect
from apps.to_dolists.models import ToDolist
# Create your views here.
def index(request):
    todo = ToDolist.objects.all().filter(user = request.user).order_by('-id')
    if request.method == 'POST':
        if 'add' in request.POST:
            title = request.POST.get('title')
            date = request.POST.get('date')
            Todonew = ToDolist.objects.create(title = title, date = date, user = request.user)
            Todonew.save()
            return redirect('index')
        if 'delete' in request.POST:
            list_id = request.POST.get('id')
            lists = ToDolist.objects.get(id = list_id)
            lists.delete()
            return redirect('index')
    context = {
        'todo' : todo,
    }
    return render(request, 'index2.html', context)

def update(request,id):
        todo = ToDolist.objects.get(id = id)
        if request.method == "POST":
                try:
                    title = request.POST.get('title')
                    if title :
                        todo.title = title
                        todo.save()
                        return redirect('index')
                    else:
                        return redirect('update', todo.id)
                except:
                   return redirect('update', todo.id)
        context = {
            'todo' : todo,
        }
        return render(request, 'update.html', context)


    