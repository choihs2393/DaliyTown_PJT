from django.shortcuts import render
import random

# Create your views here.
def index(request):
  return render(request, 'index.html')

def hello(request):
  pick = random.sample(range(1, 46), 6)
  return render(request, 'hello.html', context={
    'pick': pick,
  })

def iam(request):
  return render(request, 'iam.html')

def hi(request, name):
  return render(request, 'hi.html', context={
    'name': name,
  })

def add(request, prev, next):
  return render(request, 'add.html', context={
    'result': prev+next,
  })