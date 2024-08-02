# myproject/views.py
from django.shortcuts import redirect,render

def initial_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('login')