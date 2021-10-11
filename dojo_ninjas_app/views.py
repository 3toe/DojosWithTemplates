from django.db import reset_queries
from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
   context = {
      "Dojos" : Dojo.objects.all(),
      "Ninjas" : Ninja.objects.all()
   }
   return render(request, "index.html", context)

def process(request):
   if "DojoButton" in request.POST:
      if request.POST['name'] == "" or request.POST['city'] == "" or request.POST['state'] == "":
         return redirect('/')
      Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
      return redirect('/')
   if "NinjaButton" in request.POST:
      if request.POST['sel_dojo'] == "" or request.POST['Fname'] == "" or request.POST['Lname'] == "":
         return redirect('/')
      Ninja.objects.create(dojo = Dojo.objects.get(id=request.POST['sel_dojo']), first_name = request.POST['Fname'], last_name = request.POST['Lname'])
      return redirect('/')