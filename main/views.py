from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Todos
from .forms import TodosForm, RegisterForm


@login_required(login_url="/login")
def home(request):
    todos = Todos.objects.order_by('-created')
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    todos = Todos.objects.filter(Q(name__icontains=q))

    if request.method == 'POST':
        delete = request.POST.get('delete')

        if delete:
            post = Todos.objects.filter(id=delete).first()
            post.delete()

    context = {'todos': todos}
    return render(request, 'main.html', context)


@login_required(login_url="/login")
def create(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)

        if form.is_valid():
            todos = form.save()
            todos.author = request.user
            todos.save()
            return redirect('home')
    else:
        form = TodosForm()

    context = {'form': form}
    return render(request, 'create.html', context)


@login_required(login_url="/login")
def edit(request, pk):
    post = Todos.objects.get(id=pk)

    if request.method == 'POST':
        form = TodosForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodosForm(instance=post)

    context = {'post': post, 'form': form}
    return render(request, 'edit.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)
