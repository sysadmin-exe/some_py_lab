from django.shortcuts import render
from django.http import HttpResponse
from .models import feature

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
  feature1 = feature()
  feature1.id = 0
  feature1.name = 'Fast'
  feature1.is_true = True
  feature1.details = 'Our services are very fast'

  feature2 = feature()
  feature2.id = 1
  feature2.name = 'Secure'
  feature2.is_true = True
  feature2.details = 'You dont need to worry about attacks as we solve that issue'

  feature3 = feature()
  feature3.id = 2
  feature3.name = 'Available'
  feature3.is_true = False
  feature3.details = 'There is an SLA of 99.9999999%'

  feature4 = feature()
  feature4.id = 3
  feature4.name = 'Affordable'
  feature4.is_true = True
  feature4.details = 'You only pay for what you use'

  feature5 = feature()
  feature5.id = 4
  feature5.name = 'Integrity'
  feature5.is_true = True
  feature5.details = 'Trust the product always'

  features = [feature1, feature2, feature3, feature4, feature5]

  return render(request, 'onepage.html', {'features': features})