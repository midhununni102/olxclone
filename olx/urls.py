from django.urls import path
from olx import views


urlpatterns = [
    path("register",views.SignUpView.as_view(),name='signup'),
    path("login",views.LoginView.as_view(),name="signin"),
    path("",views.IndexView.as_view(),name="home"),
    path("logout/",views.logout_view,name="signout")
   
]
