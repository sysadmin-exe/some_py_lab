from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  name = 'Victor'
  context = {
    'name': 'Treasure',
    'age': 23
  }
  return render(request, 'index.html', context)