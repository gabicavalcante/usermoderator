from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .forms import UserForm

def user_new(request): 
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.status = 0
            user.save()
            form = UserForm()
            return render(request, 'account/user_form.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'account/user_form.html', {'form': form})

@csrf_protect
@login_required
def index(request):
    return render(request, 'account/index.html')