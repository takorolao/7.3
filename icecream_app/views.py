from django.shortcuts import render
from .models import Parent

def home(request):
    data = Parent.objects.all
    return render(request, 'home.html',{"data" : data} )

