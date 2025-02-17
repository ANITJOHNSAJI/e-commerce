from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from eapp import views

urlpatterns = [
  path('userlogin',views.userlogin,name='userlogin'),
  path('signup',views.usersignup,name='usersignup'),
  path('sellersignup',views.sellersignup,name='sellersignup'),
  path('sellerlogin',views.sellerlogin,name='sellerlogin'),
  path('firstpage',views.firstpage,name='firstpage'),
  path('forgotpassword',views.getusername,name='forgotpassword'),
  path('verifyotp',views.verifyotp,name='verifyotp'),
  path('passwordreset',views.passwordreset,name='passwordreset'),
  path('',views.index,name='index'),
  path('logout',views.logoutuser,name="logout"),
  path('logoutseller',views.logoutseller,name="logoutseller"),
  path('add',views.add,name="add"),
  path('delete_g/<int:id>',views.delete_g,name="delete_g"),
  path('edit_g/<int:id>',views.edit_g,name="edit_g"),
  path('product/<int:id>/', views.product, name='product'),
  path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
  path('cart/', views.view_cart, name='cart'), 
  path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
  path('buy-now/<int:id>/', views.buy_now, name='buynow'),
  path('checkout/', views.checkout, name='checkout'),
  path('order_success/', views.order_success, name='order_success'),
  path('product1/<int:id>/', views.product1, name='product1'),  


   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
