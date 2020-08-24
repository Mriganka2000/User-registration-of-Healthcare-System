from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')

# def contact(request):
#     return render(request, 'home/contact.html')


def services(request):
    return render(request, 'home/services.html')


def faq(request):
    return render(request, 'home/faq.html')


def team(request):
    return render(request, 'home/team.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")

    return render(request, 'home/contact.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("Form valid")
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            form.save()
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "home/register.html", {'form': form})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect("home")

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'home/userlogin.html', context)


def userlogout(request):
    logout(request)
    return render(request, "home/userlogout.html", {})
