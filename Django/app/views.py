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



from django.shortcuts import render, redirect

def dashboard(request):
    
    if 'todo_list' not in request.session:
        request.session['todo_list'] = []
    
    if request.method == 'POST':
       
        new_task = request.POST.get('task', '').strip()
        if new_task:  
           
            request.session['todo_list'].append(new_task)
            request.session.modified = True   
        return redirect('dashboard')   
    
    todo_list = request.session['todo_list']

    return render(request, "app/dashboard.html", {
        'title': 'Dashboard',
        'todo_list': todo_list,
    })
