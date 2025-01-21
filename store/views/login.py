from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models import Customer


class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get("return_url") # getting data throug get method everything after question mark
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
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url) # HttpResponseRedirect used when redirecting through urls
                else:
                    Login.return_url=None
                    return redirect("index")
            else:                
                error_message="Invalid Email or Password"
        else:
            error_message="Invalid Email or Password"   

        return render(request,"login.html",{'error':error_message, 'Email':email})