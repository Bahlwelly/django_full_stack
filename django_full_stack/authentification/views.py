from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import loginForm, registerForm
from .models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import Group

# Create your views here.
def login (request) :
    if request.method == 'POST' :
        form = loginForm(request.POST)

        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username= username, password = password)
            if user is None :
                form.add_error(None, "Cet utilisateur n'existe pas")
            else :
                auth_login(request, user)
                return redirect('home')

        else :
            messages.error(request, "Le nom ou le mot de pass sont invalides")
            return render(request, 'login.html', {'form' : form})   
    else :
        form = loginForm()
        return render(request, 'login.html', {'form' : form})



def register_view (request) :
    if request.method == "GET" :
        form = registerForm()
        return render(request, 'register.html', {'form' : form})
    
    else :
        form = registerForm(request.POST)
        if form.is_valid() :
            user = form.save()
            role = form.cleaned_data['role']
            group = Group.objects.get(name = role)
            user.groups.add(group)

            messages.success(request, "Le nouveau utilisateur ete cree avec succes")
            return redirect('login')
        
        else:   
            return render(request, 'register.html', {'form': form})