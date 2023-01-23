from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))



    class Meta:
        model=User
        fields=["email","username","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),

           
        
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class UpdateUserForm(forms.ModelForm):
    user= forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['user', 'address']


class UpdateProfileForm(forms.ModelForm):
    profile = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = UserProfile
        fields = ['profile', 'phone']