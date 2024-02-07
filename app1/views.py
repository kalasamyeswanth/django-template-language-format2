from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def happy(request):
    return render(request,'honey.html',{'a':'madhu priya','b':'amma', 'c':'sowji','d':'nenu'})
