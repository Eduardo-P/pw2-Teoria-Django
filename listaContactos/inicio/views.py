from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [5, 15, 25, 33, 42, 55, 65],
        }
    return render(request, "home.html" , myContext)

def anotherView(request):
    return HttpResponse('<h1>Sólo otra página</h1>')