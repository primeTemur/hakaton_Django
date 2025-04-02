from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    pass

class LoginView(View):
    def get(self,request):
        form=CustomLoginForm()
        return render(request,"accounts/login.html",context={
            'form':form
        })

    def post(self,request):
        form=CustomLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(request,username,password)

            if user:
                login(request,user)
                return redirect('home')
            
        return render(request,"accounts/login.html",context={
            'form':form
        })