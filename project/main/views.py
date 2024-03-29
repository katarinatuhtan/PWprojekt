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

    def get_queryset(self):
        queryset = Projekt.objects.all()
        naziv_parametar = self.request.GET.get('naziv', None)

        if naziv_parametar:
            queryset = queryset.filter(naziv__icontains=naziv_parametar)

        return queryset.distinct() 

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
    
class ProjektListView(ListView):
    model = Projekt
    template_name ='projekti_list.html'
    context_object_name = 'projekti'

class ProjektCreateView(CreateView):
    model = Projekt
    form_class = ProjektForm
    template_name = 'add_projekt.html'
    success_url = reverse_lazy('main:projekt')

class ProjektUpdateView(UpdateView):
    model = Projekt
    form_class = ProjektForm
    template_name = 'update_projekt.html'
    success_url = reverse_lazy('main:projekt')

class ProjektDeleteView(DeleteView):
    model = Projekt
    template_name = 'delete_projekt.html'
    success_url = reverse_lazy('main:projekt')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = self.get_object()
        return context
    
class SkupineListView(ListView):
    model = Volonterska_skupina 
    template_name ='skupine.html'
    context_object_name = 'skupinas'

class SkupinaCreateView(CreateView):
    model = Volonterska_skupina
    form_class = SkupinaForm
    template_name = 'add_skupina.html'
    success_url = reverse_lazy('main:skupina')

class SkupinaUpdateView(UpdateView):
    model = Volonterska_skupina
    form_class = SkupinaForm
    template_name = 'update_skupina.html'
    success_url = reverse_lazy('main:skupina')

class SkupinaDeleteView(DeleteView):
    model = Volonterska_skupina
    template_name = 'delete_skupina.html'
    success_url = reverse_lazy('main:skupina')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main'] = self.get_object()
        return context