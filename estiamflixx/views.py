from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from  .forms import AddSerie
from .models import Serie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
from . import forms
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,"estiamflixx/index.html")
def inscription(request):
    form=forms.SignupForm()
    if request.method == 'POST':
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,"estiamflixx/inscription.html",context={'form':form})
def connexion(request):
    if request.method=="POST":
         email=request.POST('email')
         mdp=request.POST('mdp')
         user=authenticate(password=mdp,email=email )
         if user is not None:
             return redirect("/")
         else:
             return render(request,"connexion.html")

    form=UserCreationForm(request.POST)
    context={'form':form}
    return render(request,"estiamflixx/connexion.html")

def serie(request):
    series=Serie.objects.all()
    obj={
        "liste":series
    }
    return render(request, "estiamflixx/series.html",obj)

def add_serie(request):
    if request.method=="POST":
        form=AddSerie(request.POST).save()
        return redirect('/series')
    else:
         form = AddSerie()
    return render(request, "estiamflixx/addserie.html", {'form': form,'dataSerie':Serie.objects.all})