from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
        
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def cadastrar_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            #logica criacao
            form.save()
            return redirect('login')
        
    else: 
        form = CadastroForm()
    return render(request, 'cadastrar.html', {'form':form})