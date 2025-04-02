from django.shortcuts import render
from django.views import View

from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    pass

class LoginView(View):
    def get(self,request):
        form=AuthenticationForm()
        return render(request,"accounts/login.html",context={
            'form':form
        })

