from django.shortcuts import render

# Create your views here.
from booktest.models import *


def index(request):
    return render(request, 'booktest/index.html')


def editor(request):
    return render(request, 'booktest/editor.html')


def show(request):
    goods = GoodsInfo.objects.get(pk=1)
    context = {'g': goods}
    return render(request, 'booktest/show.html', context)
