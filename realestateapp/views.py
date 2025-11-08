from django.shortcuts import render

# Create your views here.
def return_name(request):
    age=36
    return render(request,'moataz.html',{'age':age})

# Create ola page
def return_name_ola_page(request):
    age=30
    name='Ola'
    context = {'age':age , 'name':name}

    return render(request,'ola.html',context)