from django.shortcuts import render

# Create your views here.
def landing(request):
    title = 'Welcome to Integrative Health'
    return render(request, 'landing/landing.html', {'title':title})
