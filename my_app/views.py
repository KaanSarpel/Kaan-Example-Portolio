from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
  return render(request,'my_app/home.html')

def about(request):
  return render(request,'my_app/about.html')

def work(request):
  return render(request,'my_app/work.html')

def contact(request):
  if request.method == 'POST':
    email = request.POST['email']
    message = request.POST['message']

    send_mail(email,
    message,
    settings.EMAIL_HOST_USER,
    ['sarpelkaan_17@hotmail.com'],
    fail_silently=False)
    messages.success(request, 'Your message has successfully been sent!')
    return redirect('home')

  return render(request,'my_app/contact.html')
