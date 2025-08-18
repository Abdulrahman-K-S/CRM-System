from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, CreateClientForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    return render(request, 'web/dashboard.html')


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