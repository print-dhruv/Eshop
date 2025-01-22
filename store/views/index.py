from django.shortcuts import render, redirect
from django.views import View
from store.models import Product, Categories

class Index(View):
    # GET METHOD
    def get(self,request):
        cart = request.session.get("cart",{})
        categories= Categories.objects.all()
        category_id = request.GET.get('category')
        
        if category_id: # when a particular category is selected
            products = Product.objects.filter(category=category_id)
        else: # when all category is selected
            products = Product.objects.all()

        context={
            'products':products,
            'categories':categories,
            'cart': cart
        }
        # print(request.session.get('session_id')," ", request.session.get('session_email') )
        return render(request,'index.html',context)
    
    #POST METHOD
    def post(self,request):     
        # getting cart from customer's unique session id
        cart = request.session.get('cart',{})       
        product_id = request.POST.get('product_id')
        remove = request.POST.get('remove')

        if remove:
            cart.pop(product_id)
        else:
            cart[product_id] = 1
                
        #saving the cart progress
        request.session['cart'] = cart

        print(request.session['cart'])
        return redirect('index')   