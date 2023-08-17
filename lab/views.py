from django.shortcuts import render,HttpResponse
from lab.models import Lab
from patient.models import Patient



def home(request):
    data={
       'title' : 'LIMS'
    }
    return render(request,'index.html',data)
def index(request):
    return render(request,'patient.html')
def registration(request):
     if request.method =="post":
      pass
     else:
      return render(request,'index.html',
                    {'labs':Lab.objects.all()})

def lab_login(request):
     return render(request,'index.html')
def patient_login(request):
    if request.method =="post":
     
     name =request.POST.get("name")
     labs =request.POST.get("lab")
     return HttpResponse("This is login page")
    else:
        return render(request,'index.html')
