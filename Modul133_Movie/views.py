from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

"""
Hier werden die Funktionen aufgelistet, die während des Renderings in der urls.py aufgerufen werden.
ein solches beispiel ist die neuste seite  path('accounts/logout', views.logout_view, name='logout').
Weiter unten ist besagte view erstellt worden und kann daher ebenfalls gerendered werden.
"""

def home(request):
    return render(request, 'home.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'registration/logout.html')