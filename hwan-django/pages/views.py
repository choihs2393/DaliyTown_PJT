from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def hello(request):
  import random
  pick = random.sample(range(1, 46), 6)
  return render(request, 'hello.html', context={
    'pick': pick,
  })

def iam(request):
  return render(request, 'iam.html')