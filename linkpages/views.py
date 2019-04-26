from django.shortcuts import render
from django.http import HttpResponse



from django.contrib.auth.models import User

# Create your views here.


def index(request):

	page = "Home"
	title = "Home - " + page

	context = {"title": title}

	return render(request, 'index.html', context)

def test(request):

	page = "test"
	title = "test"

	context = {"title": title}

	return render(request, 'test.html', context)