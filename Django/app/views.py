from django.shortcuts import render
 

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

def dashboard(request):
   return render(request, "app/dashboard.html",
      {
         'title':'Dashboard',
     })