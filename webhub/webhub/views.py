from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render


def home(request):
    return render(request,"index.html")

def work(request):
    return render(request,"work.html")

def about(request):
    return render(request,"about.html")

