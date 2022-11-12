from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import get_object_or_404
import uuid

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def about(request):
    return render(request,'app/about.html')




def contact_us(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub= request.POST.get('subject')
        msg = request.POST.get('message')

        obj =Conatct(name=name,email=email,subject=sub,message=msg)
        obj.save()
        messages.success(request,f'dear {name} ,Thanks for time!')

    return render(request,'app/contact.html')


def feature(request):
    return render(request,'app/feature.html')


def menu(request):
    burger=Dish.objects.filter(category='Burger')
    pizza=Dish.objects.filter(category="Pizza")
    snacks=Dish.objects.filter(category="Snacks")
    sweet=Dish.objects.filter(category='sweet')
    context={
        'burger':burger,
        'pizza':pizza,
        'snacks':snacks,
        'sweet':sweet,
    }

    return render(request,'app/menu.html',context)


def booking(request):
    return render(request,'app/booking.html')


def team(request):
    chef= Team.objects.all()
    return render(request,'app/team.html',{'chef':chef})


def blog(request):
    return render(request,'app/blog.html')


def single(request):
    return render(request,'app/single.html')

def order(request):
    return render(request,"app/ordere.html")


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        number = request.POST.get('number')

        check=User.objects.filter(username=email)
        if len(check)==0:
            usr = User.objects.create_user(email,email,password)
            usr.first_name=name
            usr.save()

            profile=Profile(user=usr,contact_number=number)
            profile.save()
            messages.success(request,f"User {name} Registered Successfully!")
        else:
            messages.success(request, f"User {name} Already  Registered !")


    return render(request,'app/registration.html')
def signin(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser or user.is_staff:
                return redirect('admin')
            return redirect('dashboard')
        else:
            return redirect('registration')

    return render(request,'app/login.html')
def dashboard(request):
    login_user= get_object_or_404(User,id=request.user.id)
    profile=Profile.objects.get(user_id=request.user.id)
    context ={
        'profile':profile
    }
#update profile
    if "update_profile" in request.POST:
        name=request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')

        profile.user.first_name=name
        profile.user.save()
        profile.contact_number=contact_number
        profile.address=address
        if "profile_pic" in request.FILES:
            pic=request.FILES['profile_pic']
            profile.profile_pic=pic
        profile.save()
        context['status'] = 'Profile Update Successfully!'
# change password
    if "change_pass" in request.POST:
        c_password=request.POST.get('current_password')
        n_password=request.POST.get('new_password')
        check=login_user.check_password(c_password)

        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request,login_user)
            context['status'] = 'Password  Update Successfully!'
        else:
            context['status'] = 'Current Password Incorrect!'



    return render(request,'app/dashbord.html',context)
###logou
def user_logout(request):
    logout(request)
    return redirect('home')

###forget password
def token(request):
    return render(request,'app/token.html')

def changepassword(request,token):
    context = {}
    try:
        profile_obj = Forget.objects.get(forget_password_token=token)
        print(profile_obj)

    except Exception as e:
        print(e)

    return render(request, 'app/password_reset.html')

def forget_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username')
                return redirect('forgot')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            send_forget_password_mail(user_obj, token)
            messages.success(request, 'An email is send')
            return redirect('changepassword')


    except Exception as e:
        print((e))
    return render(request,'app/change_password_confirm.html')


def send_forget_password_mail(email, token):
    subject = 'Your forget Password link'
    message = f'Hi,click on the link to reset password http://127.0.0.1:8000/change_password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

