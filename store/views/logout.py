from django.views import View
from django.shortcuts import redirect

class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect('index')