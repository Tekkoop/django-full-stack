from django.shortcuts import render, HttpRespone

# Create your views here.
def say_hello(request):
    return HttpRespone("Hello!")