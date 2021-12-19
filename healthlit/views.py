from django.shortcuts import render, redirect
from .models import Program, ConfirmedCase
from django.contrib import messages
from django.utils import timezone

def healthlitIndex(request):
    #programsList =['Vascular Health', 'Osteoarthritis Health', 'Oral Health', 'Respiratory Health', 'Cognitive Health']
    programsList = Program.objects.all()
    if request.method == 'POST':
        if request.POST.get("eduPage") is not None:
            eduPage = "healthlit/"
            eduPage += request.POST.get("eduPage")
            eduPage += ".html"
            print(eduPage)
            return render(request, eduPage)
        else:
            con = request.POST.get("pat-confirmed")
            print(con)
            hold = ConfirmedCase(patName=con, patProgram="vascular")
            hold.save()
            newline = '\n'
            messages.success(request, 'ขอบคุณค่ะสำหรับข้อมูล พยาบาลผู้จัดการส่วนตัวคุณจะศึกษารายละเอียดส่วนตัวคุณและติดต่อกลับคุณโดยเร็วค่ะ ถ้าไม่ได้รับการติดต่อกลับภายใน 1 วัน กรุณาโทรแจ้ง คุณรัตนา')
            return render(request, 'healthlit/main.html', {'lists' : programsList})
    return render(request, 'healthlit/main.html', {'lists': programsList})

def subprogramIndex(request):
    return render(request, 'healthlit/submain.html')

def confirmedCases(request):
    return 
