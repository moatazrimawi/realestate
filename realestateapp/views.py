from django.shortcuts import render

# Create your views here.
def return_name(request):
    age=36
    return render(request,'moataz.html',{'age':age})