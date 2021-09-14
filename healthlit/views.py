from django.shortcuts import render
from .models import Program

def healthlitIndex(request):
    #programsList =['Vascular Health', 'Osteoarthritis Health', 'Oral Health', 'Respiratory Health', 'Cognitive Health']
    programsList = Program.objects.all()
    return render(request, 'healthlit/main.html', {'lists': programsList})
