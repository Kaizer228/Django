from django.shortcuts import render, redirect
from django import forms


tasks = []  


class AddTaskForm(forms.Form):

    task = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Add your task here...',
        })
    )

    date = forms.DateField(
       
        widget=forms.DateInput(attrs={
            'class': 'w-full p-3 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Select a date',
            'type': 'date' 
        })
    )

    priority = forms.ChoiceField(
        choices=[('Urgent', 'Urgent'), ('Not Urgent', 'Not Urgent'), ('Not Important', 'Not Important')],
        widget=forms.Select(attrs={
            'class': 'w-full p-3 mb-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
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
            priority = form.cleaned_data["priority"]

            tasks.append({"task": task, "date": date, "priority" : priority})
            return redirect('dashboard')

    else:
        form = AddTaskForm()

    return render(request, "app/dashboard.html", {
        'title': 'TODO-LIST',
        'tasks': tasks,
        'form': form
    })