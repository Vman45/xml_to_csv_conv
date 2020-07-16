from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Request
from .forms import RequestForm


def home(request):

	all_requests = Request.objects.all

	return render(request, 'home.html', {'requests': all_requests})


def add_request(request):

	if request.method == 'POST':
		form = RequestForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Request has been made.'))
			return redirect('home')
		else:
			messages.success(request, ('Something went wrong...'))
			return render(request, 'add_request.html', {})
	else:
		return render(request, 'add_request.html', {})
