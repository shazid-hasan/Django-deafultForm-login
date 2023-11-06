from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def registrations(request):
    if request.method == "POST":
        user_form=UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
           
            return HttpResponse("successful registration")
    else:
        user_form=UserCreationForm()
    return render(request,'registration.html',{'user_form':user_form})    