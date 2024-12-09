from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginForm

def signup_view(request):  # Cadastro
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):  # Login
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):  # Logout
    logout(request)
    return redirect('home')  # Redireciona para a página inicial após o logout