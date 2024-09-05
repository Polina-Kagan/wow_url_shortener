from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def home(request):
    return render (request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
        
def about(request):
    return render(request, 'users/about.html')