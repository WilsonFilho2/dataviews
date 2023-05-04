from django.shortcuts import render
from django.http import request

# Create your views here.

dt = [
        15339,
        21345,
        18483,
        24003,
        23489,
        34092,
        22034
    ]

def index(request):
    return render(request, 'dashboard/index.html', 
    {
        'dtpy': dt
        })
