from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('join/', views.VolonterCreateView.as_view(), name='join'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('volonter/', views.VolonterListView.as_view(), name='volonter'),
    path('projects/', views.ProjektiListView.as_view(), name='projects'),
    path('crud/', views.CrudPageView.as_view(), name='crud'),
    path('updatevolonter/<int:pk>', views.VolonterUpdateView.as_view(), name='updatevolonter'),
    path('deletevolonter/<int:pk>', views.VolonterDeleteView.as_view(), name='deletevolonter'),
    path('addprojekt/', views.ProjektCreateView.as_view(), name='addprojekt'),
    path('projektlist/', views.ProjektListView.as_view(), name='projektlist'),
    path('updateprojekt/<int:pk>', views.ProjektUpdateView.as_view(), name='updateprojekt'),
    path('register/', views.register, name='register'),
]