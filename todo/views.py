from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
  
def index(request):
    if request.GET.get('clear') == 'clear':
        request.session.clear()
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"index.html",{"tasks":request.session["tasks"]})
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request,"add.html",{
                "form" : form
            })
    return render(request,"add.html",{
        "form" : NewTaskForm()
    })