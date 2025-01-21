from django.views import View
from django.shortcuts import render
from ..models import Product


class Cart(View):
    def get(self,request):
        cart =request.session.get('cart',{})
        cart_product_ids = list(cart.keys())

        cart_products_queryset=Product.objects.filter(id__in=cart_product_ids)
        context = {
            'cart_products':cart_products_queryset,
            'cart':cart,
        }
        return render(request,'cart.html',context)
