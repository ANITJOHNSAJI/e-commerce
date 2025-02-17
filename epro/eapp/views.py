

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
import random
from datetime import datetime, timedelta
from.models import *
from django.contrib.auth.decorators import login_required

# user homepage
def index(request):
    # return render(request, 'index.html')
    gallery_images = Gallery.objects.all()
    return render(request, "index.html", {"gallery_images": gallery_images})

def usersignup(request):
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        
        if not username or not email or not password or not confirmpassword:
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('userlogin') 

    return render(request, "register.html")

def userlogin(request):
    if 'username' in request.session:
        return redirect('index')  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('index')  
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'userlogin.html')

def product(request, id):
    gallery_images = Gallery.objects.filter(pk=id)
    return render(request, 'product.html', {"gallery_images": gallery_images})


@login_required
def add_to_cart(request, id):
    product = Gallery.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
    )
    if not created:
        cart_item.quantity += 1  
        cart_item.save()

        return redirect('cart')  
    # else:
    #     cart_item.save()
    #     return redirect('userlogin') 


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {"cart_items": cart_items})

def remove_from_cart(request, id):
    
    item = get_object_or_404(Cart, id=id)
    item.delete()  
    return redirect('cart')  

def product1(request, id):
    gallery_images = Gallery.objects.filter(pk=id)
    return render(request, 'product.html', {"gallery_images": gallery_images})

@login_required
def buy_now(request, id):
    product = Gallery.objects.get(id=id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
    )
    cart_item.quantity += 1  
    cart_item.save()
    return redirect('checkout')
  

@login_required
def checkout(request):
    
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.quantity * item.quantity for item in cart_items)  

    
    if request.method == 'POST':
        cart_items.delete()  
        return redirect('order_success')  # Redirect to a success page or payment gateway

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def order_success(request):
    return render(request, 'order_success.html')





def sellersignup(request):
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Validate form fields
        if not username or not email or not password or not confirmpassword:
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('sellerlogin')  # Redirect to login page

    return render(request, "sellerregister.html")

def sellerlogin(request):
    if 'username' in request.session:
        return redirect('firstpage')  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            if user.is_staff:
                return redirect('firstpage')
            return redirect('index')  # Redirect to the home page
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('firstpage')

    return render(request, 'sellerlogin.html')

# seller homepage
def firstpage(request):
   
    gallery_images = Gallery.objects.filter(user=request.user)
    return render(request,'firstpage.html',{"gallery_images": gallery_images})
    # # return render(request, 'firstpage.html')
    # data = Gallery.objects.all()  # Default value for data
    
    # if request.method == 'POST':
    # #     # Handle POST logic
    #     todo123 = request.POST.get("todo")
    #     todo321 = request.POST.get("date")
    #     todo311 = request.POST.get("course")
        
    #     obj = Gallery(title1=todo123, title2=todo321, title3=todo311)
    #     obj.save()
    #     return redirect('firstpage')  # Redirect after saving the data

    # # Handle GET request
    # gallery_images = Gallery.objects.all()
    # return render(request, "firstpage.html", {"gallery_images": gallery_images, "feeds": data})

# product adding page
def add(request):
    if request.method == 'POST' and 'image' in request.FILES:  # Ensure the 'image' key is in request.FILES
        myimage = request.FILES['image']  # Access the uploaded image from request.FILES
        # Create an instance of Gallery and save the image  # Save the object to the database
        # return redirect('index')  # Redirect back to the index page after saving
        todo123=request.POST.get("todo")
        todo321=request.POST.get("date")
        todo311=request.POST.get("course") 
        todo333=request.POST.get("quant") 
        obj=Gallery(title1=todo123,title2=todo321,title3=todo311,quantity=todo333,feedimage=myimage,user=request.user)
        obj.save()
        data=Gallery.objects.all()



def verifyotp(request):
    if request.POST:
        otp = request.POST.get('otp')
        otp1 = request.session.get('otp')
        otp_time_str = request.session.get('otp_time')  # This is now a string, not a datetime object

        # Check if OTP is expired
        if otp_time_str:
            otp_time = datetime.fromisoformat(otp_time_str)  # Convert the string back to a datetime object
            otp_expiry_time = otp_time + timedelta(minutes=5)  # OTP expires after 5 minutes
            if datetime.now() > otp_expiry_time:
                messages.error(request, 'OTP has expired. Please request a new one.')
                del request.session['otp']
                del request.session['otp_time']
                return redirect('verifyotp')  # Redirect to request a new OTP

        if otp == otp1:
            del request.session['otp']
            del request.session['otp_time']
            return redirect('passwordreset')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    # Generate OTP and send email
    otp = ''.join(random.choices('123456789', k=6))
    request.session['otp'] = otp
    request.session['otp_time'] = datetime.now().isoformat()  # Store the current time as an ISO string
    message = f'Your email verification code is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.session.get('email')]
    send_mail('Email Verification', message, email_from, recipient_list)

    return render(request, "otp.html")





def getusername(request):
    if request.POST:
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            request.session['email'] = user.email
            return redirect('verifyotp')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('getusername')

    return render(request, 'getusername.html')

def passwordreset(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Check if the passwords match
        if confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        else:
            email = request.session.get('email')
            try:
                user = User.objects.get(email=email)

                # Set the new password
                user.set_password(password)
                user.save()

                # After resetting password, clear the session email
                del request.session['email']
                messages.success(request, "Your password has been reset successfully.")
                
                # Optionally, log the user in automatically after resetting the password
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)

                return redirect('userlogin')  # Redirect to the login page after password reset
            except User.DoesNotExist:
                messages.error(request, "No user found with that email address.")
                return redirect('getusername')  # Redirect to username input form

    return render(request, "passwordreset.html")

def logoutuser(request):
    logout(request)
    request.session.flush()
    return redirect(userlogin)

def logoutseller(request):
    logout(request)
    request.session.flush()
    return redirect(sellerlogin)

def delete_g(request,id):
    feeds=Gallery.objects.filter(pk=id)
    feeds.delete()
    return redirect('firstpage')

def edit_g(request,id):
      if request.method == 'POST':
        # Check if the image is provided in the request
        myimage = request.FILES.get('image')
        
        # Get the form data (title, date, course)
        todo123 = request.POST.get("todo")
        todo321 = request.POST.get("date")
        todo311 = request.POST.get("course")
        
        # Ensure all fields are populated before updating
        if todo123 and todo321 and todo311:
            # Update the Gallery record if all fields are valid
            gallery_instance = get_object_or_404(Gallery, pk=id)
            gallery_instance.title1 = todo123
            gallery_instance.title2 = todo321
            gallery_instance.title3 = todo311
            if myimage:  # Update the image only if provided
                gallery_instance.feedimage = myimage
            gallery_instance.user = request.user
            gallery_instance.save()

            # Redirect to 'firstpage' after successful update
            return redirect('firstpage')
        else:
            # If fields are missing, you can return an error message or re-render the form
            return render(request, 'add.html', {
                'error': "All fields must be filled out.",
                'data1': get_object_or_404(Gallery, pk=id)
            })

      else:
        # GET request: Fetch the gallery image for editing
        gallery_images = get_object_or_404(Gallery, pk=id)
        return render(request, 'add.html', {'data1': gallery_images})
    # if request.method == 'POST' and 'image' in request.FILES:
    #     myimage = request.FILES['image']
    #     todo123=request.POST.get("todo")
    #     todo321=request.POST.get("date")
    #     todo311=request.POST.get("course")
    #     Gallery.objects.filter(pk=id).update(title1=todo123,title2=todo321,title3=todo311,feedimage=myimage,user=request.user)
    #     return redirect('firstpage')
    # else:
    #     gallery_images=Gallery.objects.get(pk=id)
    #     return render(request,'add.html',{'data1':gallery_images})




