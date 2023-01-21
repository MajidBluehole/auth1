from django.shortcuts import render,redirect
from django.views import View
from .form import RegistrationForm, ProfileForm
from .models import Profile
# Create your views here.
# def index(request):
#     return render(request,'index.html')

class Registration(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'index.html',{'form':form})
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'index.html',{'form':form})

class ProfileUpdate(View):
    def get(self,request):
        form = ProfileForm()
        return render(request,'profile.html',{'form':form})
    def post(self,request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            res = Profile(country=country,state=state,city=city,zipcode=zipcode,user=user)
            res.save()
            return redirect('Profle')
        return render(request,'profile.html',{'form':form})