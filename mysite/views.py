from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return HttpResponse("<b>This is current top page but under construction...</b>")
