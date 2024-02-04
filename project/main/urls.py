from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    # path('add/', views.IceCreamCreateView.as_view(), name='add'),
    # path('list/', views.IceCreamListView.as_view(), name='list'),
    # path('update/', views.IceCreamUpdateView.as_view(), name='update'),
    # path('delete/', views.IceCreamDeleteView.as_view(), name='delete'),
]