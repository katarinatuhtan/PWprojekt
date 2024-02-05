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
    
class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'o_nama.html')
    
class VolonterListView(ListView):
    model = Volonter
    template_name ='volonteri.html'
    context_object_name = 'volonters'

class ProjektiListView(ListView):
    model = Projekt
    template_name = 'projekti.html'
    context_object_name = 'projekts'

class VolonterCreateView(CreateView):
    model = Volonter
    form_class = VolonterForm
    template_name = 'join.html'
    success_url = reverse_lazy('main:join')

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
    
class VolonterUpdateView(UpdateView):
    model = Volonter
    form_class = VolonterForm
    template_name = 'update_volonter.html'
    success_url = reverse_lazy('main:volonter')

class VolonterDeleteView(DeleteView):
    model = Volonter
    template_name = 'delete_volonter.html'
    success_url = reverse_lazy('main:volonter')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = self.get_object()
        return context
