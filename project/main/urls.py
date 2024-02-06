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
    path('projekt/', views.ProjektListView.as_view(), name='projekt'),
    path('addprojekt/', views.ProjektCreateView.as_view(), name='addprojekt'),
    path('updateprojekt/<int:pk>', views.ProjektUpdateView.as_view(), name='updateprojekt'),
    path('deleteprojekt/<int:pk>', views.ProjektDeleteView.as_view(), name='deleteprojekt'),
    path('register/', views.register, name='register'),
     path('skupina/', views.SkupineListView.as_view(), name='skupina'),
     path('addskupina/', views.SkupinaCreateView.as_view(), name='addskupina'),
     path('updateskupina/<int:pk>', views.SkupinaUpdateView.as_view(), name='updateskupina'),
     path('deleteskupina/<int:pk>', views.SkupinaDeleteView.as_view(), name='deleteskupina'),
]