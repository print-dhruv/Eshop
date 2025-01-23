from django.views import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ..models import Orders

class OrdersView(View):
    def get(self,request):
        session_customer_id = request.session.get('session_customer_id')       
        orders_of_customer = Orders.objects.filter(customer_id=session_customer_id).order_by('-date')
        
        #code for setting pagination    
        orders_page_pagination = Paginator(orders_of_customer,3)
        page_number = request.GET.get('page')
        final_pages = orders_page_pagination.get_page(page_number)
        #for sending last page
        last_page = orders_page_pagination.num_pages
        #just deriving get request page number from final_pages keys
        current_page = final_pages.number

        #writing logic to send before and after page to current page
        start_page = max(current_page - 1, 1)  # Start range (at least page 1)
        end_page = min(start_page + 2, last_page)  # End range (at most last page)
        list_of_page_numbers = range(start_page, end_page + 1)

        context={
            'orders':final_pages,
            'last_page':last_page,
            'list_of_page_numbers':list_of_page_numbers
        }
        return render(request,'order.html',context)