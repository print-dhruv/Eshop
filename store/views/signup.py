from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views import View
from store.models import Customer
from django.core.mail import send_mail


class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name") 
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Customer.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            contact = contact,  
                            email = email,
                            password = make_password(password))
        customer.save()
        # Data recieving mail after signup
        send_mail(
            f"customer number {Customer.objects.filter(email=email).first().id} sign In", 
            f"{first_name} {last_name} sign in with Email iD {email} and contact number {contact}",
            "dhruvdotsquares@gmail.com", # server mail id
            ["fosikej882@halbov.com",], # developer id
            False,
        )
        # Confirmation mail to customer
        send_mail(
            "Successful signIn at Eshop", 
            f"Congratulations!! {first_name} you are successfully signin as a customer in Eshop",
            "achernar009@gmail.com", # server id
            [email,], # customer id
            False
        )


        # when we redirect to index.html directly, all the things which index view was adding to this file, would be missing.
        # return render(request,'index.html')
        return redirect("login")