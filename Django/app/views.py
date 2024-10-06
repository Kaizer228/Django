from django.shortcuts import render
 

def index(request):
    return render(request, "app/index.html",
       {
         'title':'Welcome',    
     })


def login(request):
   return render(request, "app/login.html",
      {
         'title':'Login',
     })


def register(request):
    return render(request, "app/register.html",
     {
         'title':'Register', 
     })