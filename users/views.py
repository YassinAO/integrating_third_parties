from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import UserRegistrationForm

# Create your views here.


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
