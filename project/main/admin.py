from django.contrib import admin
from main.models import *

model_list = [Projekt, Volonter,Volonterska_skupina]
admin.site.register(model_list)
