from itertools import product
from django.http import HttpResponse
from django.template import loader
from .models import Farm, Product

def home(request):
    template = loader.get_template('web/home.html')
    return HttpResponse(template.render({}, request))

def farms_list(request):
    template = loader.get_template('web/farms.html')
    farms = Farm.objects.all()
    return HttpResponse(template.render({'farms': farms}, request))

def farm_detail(request):
    template = loader.get_template('web/farms.html')
    farms = Farm.objects.all()
    return HttpResponse(template.render({'farms': farms}, request))

def products_list(request):
    template = loader.get_template('web/products.html')
    products = Product.objects.all()
    return HttpResponse(template.render({'products': products}, request))