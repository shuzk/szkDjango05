from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'booktest/index.html')


def editor(request):
    return render(request, 'booktest/editor.html')