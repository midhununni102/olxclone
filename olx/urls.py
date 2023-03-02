from django.urls import path
from olx import views


urlpatterns = [
    path("register",views.SignUpView.as_view(),name='signup'),
    path("login",views.LoginView.as_view(),name="signin"),
    path("",views.IndexView.as_view(),name="home"),
    path("logout/",views.logout_view,name="signout"),
    path("add",views.ProductAddView.as_view(),name='add'),
    path("product/detail/<int:id>",views.ProductDetailView.as_view(),name='detail'),
    path('display_profile/', views.display_profile,name='display_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('noti',views.NotiView.as_view(),name='noti'),
    path('search/', views.search_view, name='search'),
    path('chatwithseller/',views.chatbot,name='chatwithseller')

    # Add any additional URL patterns here


  


   
   
   
]
