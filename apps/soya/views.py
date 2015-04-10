# coding: utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login

from models import Soyainfo, Products, Zakaz
from forms import Zakazat

def base(request):
	soyainfo = Soyainfo.objects.all()
	return render(request, 'soya/index.html', {'soyainfo': soyainfo})

def info(request):
	soyainfo = Soyainfo.objects.all()
	return render(request, 'soya/info.html', {'soyainfo': soyainfo})

def moreinfo(request, id):
	soyainfo = Soyainfo.objects.get(pk=id)
	return render(request, 'soya/moreinfo.html', {'soyainfo':soyainfo}) 

def product(request):
	products = Products.objects.all()
	return render(request, 'soya/products.html', {'products': products})

def zakazat(request):
    if request.method == 'POST':
        form = Zakazat(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = Zakazat()        
    return render(request, "soya/form.html", {'form': form})

def zakazi(request):
	zakaz = Zakaz.objects.all()
	return render(request, "soya/zakazi.html", {'zakaz': zakaz })

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return render(request, 'soya/zakazi.html')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'soya/login.html')