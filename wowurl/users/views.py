from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
def home(request):
    return render (request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('profile')  
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
        
def about(request):
    return render(request, 'users/about.html')
@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)   
    
    data = {
        'updateUserForm': updateUserForm,
    }
    return render(request, 'users/profile.html', data)