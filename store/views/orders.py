from django.views import View
from django.shortcuts import render, redirect
from ..models import Orders

class OrdersView(View):
    def get(self,request):
        session_customer_id = request.session.get('session_customer_id')       
        orders_of_customer = Orders.objects.filter(customer_id=session_customer_id).order_by('-date')
        context={
            'orders':orders_of_customer,
        }
        return render(request,'order.html',context)