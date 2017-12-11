from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'base.html',{})


def happyanniversary(request):
	return render(request,'happyanniversary.html',{})

def surprize(request):
	return render(request,'page2.html',{})

def fifteen(request):
	return render(request,'2015.html',{})

def sixteen(request):
	return render(request,'2016.html',{})

def seventeen(request):
	return render(request,'2017.html',{})


