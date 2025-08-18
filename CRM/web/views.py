from django.shortcuts import render, redirect
from .forms import RegisterUserForm


def index(request):
    return render(request, 'web/index.html')

def register(request):
    form = RegisterUserForm()
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
    else:
        form = RegisterUserForm()
    
    context = {'form': form}
    return render(request, 'web/register.html', context)
