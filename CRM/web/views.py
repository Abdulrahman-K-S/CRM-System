from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterUserForm, LoginUserForm, CreateClientForm, UpdateClientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging

from . import models


def index(request):
    return render(request, 'web/index.html')


def register(request):
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request, 'web/register.html', context)


def user_login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginUserForm()
    
    context = {'form': form}
    return render(request, 'web/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    clients = models.Client.objects.all()
    return render(request, 'web/dashboard.html', context={'clients': clients})


@login_required(login_url='login')
def create_client(request):
    form = CreateClientForm()

    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateClientForm()

    context = {'form': form}
    return render(request, 'web/create-client.html', context)


@login_required(login_url='login')
def view_client(request, client_id):
    client_object = get_object_or_404(models.Client, id=client_id)
    context = {'client': client_object}
    return render(request, 'web/view-client.html', context)


@login_required(login_url='login')
def update_client(request, client_id):
    client_object = get_object_or_404(models.Client, id=client_id)
    form = UpdateClientForm(instance=client_object)
    if request.method == 'POST':
        form = UpdateClientForm(request.POST, instance=client_object)
        if form.is_valid():
            form.save()
            return redirect('view_client', client_id=client_id)
    context = {'form': form}
    return render(request, 'web/update-client.html', context)


@login_required(login_url='login')
def delete_client(request, client_id):
    client_object = get_object_or_404(models.Client, id=client_id)
    client_object.delete()
    return redirect('dashboard')


logger = logging.getLogger(__name__)

@login_required(login_url='login')
def search_clients(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = models.Client.objects.filter(Q(client_first_name__icontains=query) | Q(id__icontains=query))
    except Exception as e:
        logger.error('Error during search_clients function: %s', e)
    return render(request, 'web/search.html', context={'results': results, 'query': query})