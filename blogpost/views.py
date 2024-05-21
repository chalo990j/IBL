from django.shortcuts import render
from django.http import HttpResponse
import email
from re import I, template


# Create your views here.
def index(request):
    template ="posted/index.html"
    return render(request, template)

def Subscribe(request):

    return render(request)