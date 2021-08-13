from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'appfo/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request,'appfo/register.html', {'form':form})


