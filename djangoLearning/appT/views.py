from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    print(request,'right here! ')
    return HttpResponse('<h1>这是返回来滴标签 嘿嘿！</h1>')
# Create your views here.

def demo2(request):
    print(request,'right here! ')
    return HttpResponse('<h1>demo2F</h1>')