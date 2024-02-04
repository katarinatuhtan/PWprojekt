from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')
    
class VolonterListView(ListView):
    model = Volonter
    template_name = 'o_nama.html'
    context_object_name = 'volonters'