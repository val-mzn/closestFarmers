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

def farm_detail(request, id):
    template = loader.get_template('web/farm_detail.html')
    farm = Farm.objects.get(id=id)
    return HttpResponse(template.render({'farm': farm}, request))

def products_list(request):
    template = loader.get_template('web/products.html')
    products = Product.objects.all()
    return HttpResponse(template.render({'products': products}, request))

def searchs_list(request, search):
    template = loader.get_template('web/searchs.html')

    farms = Farm.objects.all()
    farms_selected = []

    for farm in farms:
        if search in farm.name.lower():
            farms_selected.append(farm)
        for product in farm.products.all():
            if search in product.name.lower():
                farms_selected.append(farm)

    return HttpResponse(template.render({'searchs': farms_selected}, request))