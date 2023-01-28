from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render,redirect
from .helper import MessageHandler,MessageHandler1
from .models import Patient,Doctors,Medications,Transaction
from django.contrib import messages
import random
from django.contrib.auth import authenticate,login,logout
from .forms import PatientForm

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['Password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                otp1=random.randint(100000,999999)
                profile = Transaction.objects.get(user1 = username)
                profile.otp=otp1
                profile.save()
                print(otp1)
                messagehandler=MessageHandler(profile.phone1,profile.otp).send_otp_via_message()
                return redirect(f'/otp/{profile.uid}')
            else:
                messages.info(request,'account is not active')
                return redirect('signin')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('signin')
    else:
        return render(request,'authenticate/signin.html')

def signup(request):
    context = {}
    if request.method == "POST":
        userform = PatientForm(data=request.POST)
        phonenum = request.POST.get('phone')
        if userform.is_valid():
            user = userform.save()
            user.save()
            profile=Transaction.objects.create(user=user,phone1=user.phone,user1=user.username)
            profile.save()
            return redirect('signin')
        else:
            print(userform.errors)
            messages.info(request,userform.errors)
            return redirect('signup')
    else:
        userform=PatientForm()
    return render(request,'authenticate/signup.html',{'userform':userform})    


# def home(request):
#     parts=participants.objects.all().count()
#     users=CustomUser.objects.all().count()
#     voters=Voters.objects.all().count()
#     remaining=users-voters
#     return render(request,'authenticate/home.html',{'userform':CustomUser,'remain':remaining,'users':users,'parts':parts,'voters':voters})

def otpVerify(request,uid):
    if request.method=="POST":
        otp = request.POST.get('otp')
        profile = Transaction.objects.get(uid = uid)
        if otp == profile.otp:
            login(request,profile.user)
            return redirect('profile')
        else:
            messages.info(request,"OTP is invalid")
            return redirect('/otp/uid')
    return render(request,'authenticate/otp.html')

@login_required(login_url="/signin/")
def logout_acc(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))

@login_required(login_url="/signin/")
def profile(request):
    return render(request,'authenticate/about.html')

@login_required(login_url="/signin/")
def advice(request):
    if request.method=="POST":
        search=request.POST['search']
        parts = Medications.objects.filter(problem__startswith=search).values()
        print('1')
        print(search)
        return render(request,'authenticate/advice.html',{'parts':parts})
    else:
        parts = Medications.objects.all()
        return render(request,'authenticate/advice.html',{'parts':parts})

def home(request):
    return render(request,'authenticate/home.html')

@login_required(login_url="/signin/")
def doctor(request):
    if request.method=="POST":
        place=request.POST['place']
        cardiology=request.POST['cardiology']
        parts = Doctors.objects.filter(place__startswith=place).filter(speciality_in__startswith=cardiology).values()
        print('1')
        return render(request,'authenticate/doctors.html',{'parts':parts,'place':place,'cardiology':cardiology})
    parts=Doctors.objects.all()
    return render(request,'authenticate/doctors.html',{'parts':parts})
    
@login_required(login_url="/signin/")
def payment(request):
    if request.method=="POST":
        td=request.POST['tid']
        profile = Transaction.objects.get(user = request.user)
        profile.transaction_id=td
        profile.save()
        messagehandler=MessageHandler1(profile.phone1,profile.slot).send_otp_via_message()
        return render(request,'authenticate/sucess.html')
    return render(request,'authenticate/book.html')

@login_required(login_url="/signin/")
def sucess(request):
    return render(request,'authenticate/sucess.html')