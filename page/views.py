from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def textile(request):
    return render(request, 'textile.html')

def graphics(request):
    return render(request, 'graphics.html')

def sculpture(request):
    return render(request, 'sculpture.html')

def painting(request):
    return render(request, 'painting.html')

def ceramic(request):
    return render(request, 'ceramic.html')