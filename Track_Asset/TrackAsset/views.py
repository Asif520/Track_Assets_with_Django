from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Company, User, Company_Assets,Subscriber,Employee
from .forms import MyUserCreationForm, UserForm
from django.contrib import messages
# Create your views here.

def loginUser(request):
     page = 'login'
     if request.user.is_authenticated:
          return redirect('home')

     if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # try:
        #      user = User.objects.get(username=username)

        # except:
        #      messages.error(request, "User Dosen't Exist.")
                            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
             login(request,user)
             return redirect('home')
        else:
             messages.error(request, "Username or Password  Doesn't Exist.")

     context = {'page':page}
     return render(request, 'TrackAssets\login_register.html',context)

def logoutUser(request):
     logout(request)
     return redirect('home')

def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
         form = MyUserCreationForm(request.POST)
         if form.is_valid():
              user = form.save(commit=False)
              user.username = user.username.lower()
              user.save()
              login(request,user)
              return redirect('home')
         else:
              messages.error(request, "An Error Occured During Registration!")

    context = {'form':form}
    return render(request,'TrackAssets/login_register.html',context)

def home(request):
     q = request.GET.get('q') if request.GET.get('q') !=None else ''

     companys = Company.objects.filter(Q(name__icontains=q))

     company = Company.objects.all()

     company_assets = Company_Assets.objects.all()
     

     context = {'companys': companys, 'company': company, 'company_assets': company_assets }
     return render(request, 'TrackAssets/home.html', context)

def company(request,pk):
     company = Company.objects.get(id=pk)
     company_assets = Company_Assets.objects.all

     context = {'company':company, 'company_assets':company_assets}
     return render(request, 'TrackAssets/company.html',context)