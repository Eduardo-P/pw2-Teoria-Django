from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Hola Mundo desde Django</h1>')

def anotherView(request):
    return HttpResponse('<h1>Sólo otra página</h1>')