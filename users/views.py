from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm

def loginUser(request):
    page = 'login' #Page = yazmasının sebebi template'da if loop kullanıcak if page == 'login' loginUser else registerUser

    if request.user.is_authenticated: #Bu çok kullanışlı! Eğer user Login ise direct profiles page'e redirect ediyorum.Decorater kullanmadan.
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username) #Check If a user with this username exists.
        except:
            messages.error(request, 'Username does not exist') #Documentation Django Messages

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) #Login function creates a session for that user in the database.(User'i login ediyor.)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect') #Her bir messages'a göre styling oluşturduk.

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid(): #form.save() ==> Sadece bunuda yazıp bitirebilirdik ama aşağıdaki modifikasyon eğer user'lar arası case sensitive bir durum varsa bunu ortadan kaldırıyor.Örnek:Kaan KaAn diye 2 user oluşmasını engelliyor.
            user = form.save(commit=False) #We hold this information before processing It.
            user.username = user.username.lower() #We lower the letters of input data.
            user.save() #Then officially add user to database and save.
            messages.success(request, 'User account was created!') #Success message.
            login(request, user)
            return redirect('home')
        else:
            messages.success(
                request, 'An error has occurred during registration')
    
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

