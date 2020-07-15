from django.shortcuts import render, redirect

def home(request):

	return render(request, 'home.html', {})


def add_request(request):

	return render(request, 'add_request.html', {})
