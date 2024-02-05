from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('join/', views.VolonterCreateView.as_view(), name='join'),
    path('about/', views.VolonterListView.as_view(), name='about'),
    path('projects/', views.ProjektiListView.as_view(), name='projects'),
    # path('update/', views.IceCreamUpdateView.as_view(), name='update'),
    # path('delete/', views.IceCreamDeleteView.as_view(), name='delete'),
]