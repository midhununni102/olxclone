from django.shortcuts import render,redirect
from olx.forms import RegistrationForm,LoginForm
from django.views.generic import View,FormView,CreateView,TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class IndexView(TemplateView):
    template_name="index.html"


class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)


def home(request):
    return render(request, 'base.html') 

def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")       