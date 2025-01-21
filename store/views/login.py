from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models import Customer


class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        unverified_password = request.POST.get("password")
        email = request.POST.get("email")
        correct_password = Customer.objects.filter(email=email).values_list('password',flat=True).first()
        error_message = None
        # when email enter doesn't belong to customer but exist in database
        if correct_password:
            # Check if the unverified password matches the stored hashed password
            if check_password(unverified_password, correct_password):
                
                customer_session_object = Customer.objects.filter(email=email).first()
                request.session['session_customer_id'] = customer_session_object.id
                # Redirect to the index page on successful login
                return redirect("index")
            else:                
                error_message="Invalid Email or Password"
        else:
            error_message="Invalid Email or Password"   

        return render(request,"login.html",{'error':error_message, 'Email':email})