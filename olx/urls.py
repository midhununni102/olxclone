from django.urls import path
from olx import views


urlpatterns = [
    path("register",views.SignUpView.as_view(),name='signup'),
    path("login",views.LoginView.as_view(),name="signin"),
    path("",views.IndexView.as_view(),name="home"),
    path("logout/",views.logout_view,name="signout"),
    path("userprofile",views.UserProfileView.as_view(),name='userprofile'),
    path("add",views.ProductAddView.as_view(),name='add'),
    path("product/detail/<int:id>",views.ProductDetailView.as_view(),name='detail'),
  


   
   
   
]
