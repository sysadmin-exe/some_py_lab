from django.shortcuts import render
from django.http import HttpResponse

# Create your application function or class here.
def index(request):
  name = 'Victor'
  context = {
    'name': 'Treasure',
    'age': 23
  }
  return render(request, 'index.html', context)

def form(request):
  return render(request, 'form.html')

def counter(request):
  text = request.POST['text']
  number_of_words = len(text.split())
  return render(request, 'counter.html', {'number': number_of_words})

def api1(request):
  return render(request, 'api1.html')

def onepage(request):
  return render(request, 'onepage.html')