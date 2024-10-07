from django.shortcuts import render, redirect
from django import forms


tasks = []  




class AddTaskForm(forms.Form):
    task = forms.CharField(label="",
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Add your task here...'
        })
    )

    date = forms.DateField(
        label="",
        widget=forms.DateInput(attrs={
            'class': 'w-full p-3 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Select a date',
            'type': 'date' 
        })
    )



def dashboard(request):
  
    if 'DELETE' in request.GET:
        task_index = int(request.GET.get('DELETE')) 
        tasks.pop(task_index)  
        return redirect('dashboard') 

   
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            date = form.cleaned_data["date"]
            tasks.append({"task": task, "date": date})
            return redirect('dashboard')

    else:
        form = AddTaskForm()

    return render(request, "app/dashboard.html", {
        'title': 'Dashboard',
        'tasks': tasks,
        'form': form
    })