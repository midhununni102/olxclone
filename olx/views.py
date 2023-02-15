from django.shortcuts import render,redirect
from olx.forms import RegistrationForm,LoginForm,UserCreationForm
from django.views.generic import View,FormView,CreateView,TemplateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from olx.models import Products
from olx.forms import ProductForm
from django.http import HttpResponse



def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


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



def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")       


class UserProfileView(FormView):
    template_name="userprofile.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("home")
    
    def form_valid(self, form):
       
        messages.success(self.request,"New profile has created")
        return super().form_valid(form)  



class IndexView(ListView):
    template_name="home.html"
    context_object_name="products"
    model=Products

    

class ProductAddView(CreateView):
    template_name="productadd.html"
    form_class=ProductForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"product has been added")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"coudnt add product")
        return super().form_invalid(form)


class ProductDetailView(DetailView):
    model=Products
    template_name="productdetail.html"  
    context_object_name="product"
    pk_url_kwarg="id"  
    
      




