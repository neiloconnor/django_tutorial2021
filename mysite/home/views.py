from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        context = {'error_message': 'Invalid username or password'}
        return render(request, 'home/index.html', context)