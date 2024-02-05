from django.views import View
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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

from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/crud')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class CrudPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'crud.html')