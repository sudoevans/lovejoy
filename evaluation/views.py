# views.py
from django.shortcuts import render, redirect
from .forms import EvaluationRequestForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import EvaluationRequest
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def evaluation_request(request):
   #wantt to use EvaluationRequestForm and EvaluationRequest when the form is submitted it will redirect to the evaluation_request.html with a success message
    if request.method == 'POST':
        form = EvaluationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            #save the form
            evaluation_request = form.save(commit=False)
            evaluation_request.user = request.user
            evaluation_request.save()
            return render(request, 'evaluation_request.html', {'form': form, 'success': 'Evaluation request has been submitted'})
    else:
        form = EvaluationRequestForm()
    return render(request, 'evaluation_request.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #get the username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #check if the user is valid
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('evaluation:evaluation_request')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    context={'form': form}
    return render(request, 'login.html', context)

def admin_login(request):
    if request.method == 'POST':
        password = request.POST['password']
        if password == 'secret':
            return redirect('admin/')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid password'})
    else:
        return render(request, 'admin_login.html')
    
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Add a success message
            messages.success(request, 'Registration successful. Please log in.')

            # Redirect to the login page
            return redirect('evaluation:login')  # Replace 'login' with the actual name or URL pattern of your login view
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

