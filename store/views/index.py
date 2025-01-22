from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
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
        
        #writing pagination logic
        index_page_pagination = Paginator(products,3)
        current_page_number = request.GET.get('page')
        final_pages=index_page_pagination.get_page(current_page_number)

        last_page = index_page_pagination.num_pages

        current_page = final_pages.number
        start_page = max(1,current_page-1)
        end_page=min(start_page+2,last_page)
        list_of_page_numbers= range(start_page,end_page+1)

        context={
            'products':final_pages,
            'last_page':last_page,            
            'list_of_page_numbers':list_of_page_numbers,
            'categories':categories,
            'cart': cart,
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