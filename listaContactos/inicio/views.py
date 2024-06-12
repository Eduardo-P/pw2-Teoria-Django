from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44, 55],
        'myDate': datetime(2023, 1, 1, 12, 0),
        'variableNula': None,
        }
    return render(request, "home.html" , myContext)

def anotherView(request):
    return HttpResponse('<h1>Sólo otra página</h1>')