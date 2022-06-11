from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations, {username} ! Your account is created successfully. You can now Log in.')
            return redirect('login')
    else:    
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})
     

@login_required
def profile(request):
    return render(request, 'users/profile.html')
