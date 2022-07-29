from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Destination

# Create your views here.

class DestListView(ListView):
    model = Destination
    template_name = 'index.html'
    context_object_name = 'destinations'


