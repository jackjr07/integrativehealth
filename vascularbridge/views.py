from django.shortcuts import render
from .forms import PostRegister

def vascularBridge(request):
    title = "Vascular Bridge"
    return render(request, 'vascularbridge/base.html')


def vascularBridgeRegister(request):
    title = "Registeration"
    if request.method == 'POST':
        form = PostRegister(request.POST)
        if form.is_valid():
            form.save()
    form = PostRegister()
    return render(request, 'vascularbridge/register.html', {'form':form, 'title':title})
