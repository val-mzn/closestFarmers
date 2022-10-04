from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farms', views.farms_list, name='farms_list'),
    path('products', views.products_list, name='products_list'),
]