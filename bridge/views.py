from django.shortcuts import render
from .models import Bridge

def bridgeIndex(request):
    bridgeList = Bridge.objects.all()
    return render(request, 'bridge/main.html', {'bridgeList': bridgeList})
