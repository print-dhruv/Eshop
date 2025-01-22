from django.views import View
from django.shortcuts import render, redirect
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
    def post(self,request):
        cart = request.session.get('cart',{})
        product_id = request.POST.get('product_id')
        decrease = request.POST.get('remove')

        if decrease:
            if cart[product_id]>1:
                cart[product_id] -= 1
            else:
                cart.pop(product_id)
        else:
            cart[product_id] += 1
            
        request.session['cart'] = cart
        return redirect('cart')
