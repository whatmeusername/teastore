from django.shortcuts import render, HttpResponse, get_object_or_404
from catalog.models import product
from .cart import Cart
from django.http import JsonResponse
# Create your views here.


def AddCart(request, object_id):
    if request.method == 'POST' and request.is_ajax():
        obj = get_object_or_404(product, id = object_id)
        cart = Cart(request)
        cart.add(product = obj)
        return JsonResponse({'len': len(cart)})
    return HttpResponse('OK 200')