from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Todos
from .forms import TodosForm


def home(request):
    todos = Todos.objects.order_by('-created')

    if request.method == 'POST':
        delete = request.POST.get("delete")

        if delete:
            post = Todos.objects.filter(id=delete).first()
            post.delete()

    context = {'todos': todos}
    return render(request, 'main.html', context)


def create(request):
    form = TodosForm()

    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'create.html', context)


def view(request):
    post = Todos.objects.all()

    if request.method == 'POST':
        edit = request.POST.get("edit")

        if edit:
            post = Todos.objects.filter(id=edit).first()

    context = {'post': post}
    return render(request, 'view.html', context)
