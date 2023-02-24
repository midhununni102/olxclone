from django.shortcuts import render,redirect,get_object_or_404
from olx.forms import RegistrationForm,LoginForm,UserProfile,ProfileEditForm
from django.views.generic import FormView,CreateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from olx.models import Products
from olx.forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
decs=[signin_required,never_cache]




class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")

        return super().form_invalid(form)
    
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
                messages.success(request,"logged in successfully")
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})



def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")       



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
    
@login_required
def display_profile(request):
    user_profile = get_object_or_404(UserProfile,)
    return render(request, 'displayprofile.html', {'user_profile': user_profile})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'editprofile.html',{'form':form})




def search_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(name__contains=search)
        return render(request, "search.html", {'search':search, 'products':products})
    else:
        return render(request, "search.html")






class NotiView(IndexView):
    template_name="noti.html"