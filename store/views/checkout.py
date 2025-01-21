from django.views import View
from django.shortcuts import redirect, render
from store.models import Orders, Product, Customer


class CheckOut(View):
    def get(self, request):
        return render(request, "checkout.html")

    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer_id = request.session.get("session_customer_id")
        cart = request.session.get("cart")
        cart_product_ids = list(request.session.get("cart", {}).keys())
        cart_product_queryset = Product.objects.filter(id__in=cart_product_ids)

        for product in cart_product_queryset:
            order = Orders(
                customer_id=Customer(id=customer_id),  # from session
                product_id=product,  # product_id is a foriegn key it takes object of class
                quantity=cart.get(str(product.id)),  # from cart session
                price=product.product_price,  # from product table
                address=address,  # from post request
                phone=phone,  # from post request
            )
            order.save()
        request.session["cart"] = {}  # empty cart after checkout
        return redirect("cart")
