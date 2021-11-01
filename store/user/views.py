from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def UserLogin(request):
    data = {
        'form': LoginForm
    }
    return render(request, 'main/home.html', data)