from django.shortcuts import render
from django.http import response




def hello(request):
    raise Exception
    return response.HttpResponse("<h2> Hello </h2> \n <a href='google.com'> Google </a>")