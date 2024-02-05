from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')
    
class VolonterListView(ListView):
    model = Volonter
    template_name = 'o_nama.html'
    context_object_name = 'volonters'

class ProjektiListView(ListView):
    model = Projekt
    template_name = 'projekti.html'
    context_object_name = 'projekts'

class VolonterCreateView(CreateView):
    model = Volonter
    form_class = VolonterForm
    template_name = 'join.html'
    success_url = reverse_lazy('main:add')