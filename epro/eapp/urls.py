from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from eapp import views

urlpatterns = [
     path('',views.userlogin,name='userlogin'),
  path('signup',views.usersignup,name='usersignup'),
  path('sellersignup',views.sellersignup,name='sellersignup'),
  path('sellerlogin',views.sellerlogin,name='sellerlogin'),
  path('firstpage',views.firstpage,name='firstpage'),
  path('forgotpassword',views.getusername,name='forgotpassword'),
  path('verifyotp',views.verifyotp,name='verifyotp'),
  path('passwordreset',views.passwordreset,name='passwordreset'),
  path('index',views.index,name='index'),
  path('logout',views.logoutuser,name="logout")
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
