from django.views import View
from django.shortcuts import render

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')
    
    