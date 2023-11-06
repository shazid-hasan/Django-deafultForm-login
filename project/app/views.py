from django.shortcuts import render,HttpResponse
from .forms import RegistrationForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def registrations(request):
    if request.method == "POST":
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
           
            return HttpResponse("successful registration")
    else:
        user_form=RegistrationForm()
    return render(request,'registration.html',{'user_form':user_form})    