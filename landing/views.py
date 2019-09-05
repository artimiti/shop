from django.shortcuts import render
from .forms import SubscribersForm
from products.models import *

# Create your views here.
def landing(request):
    form = SubscribersForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
    #    print(form)
    #    print()
    #    print(request.POST)
    #    print()
    #    print(form.cleaned_data)
    #    print()
    #    data = form.cleaned_data
    #    print(data['name'])
    #    print()
    #    print(dir(form))
    #    print(request.GET)
       new_form = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
   products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
   products_images_phones = products_images.filter(product__category__id=1)
   products_images_laptops = products_images.filter(product__category__id=2)
  #  form = SubscribersForm(request.POST or None)
  #  if request.method == 'POST'and form.is_valid():
  #    new_form = form.save()
   return render(request, 'landing/home.html', locals())