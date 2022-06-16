from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
         return redirect('login')
        
    else:    
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



          
@login_required
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')
