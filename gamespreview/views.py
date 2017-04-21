from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gamespreview/home_exp.html')

def glossary(request):
	return render(request, 'gamespreview/glossary.html')

def about(request):
	return render(request, 'gamespreview/about.html')