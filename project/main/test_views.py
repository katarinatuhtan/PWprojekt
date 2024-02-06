from datetime import date
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()

        # Postavljanje URL-ova
        self.volonters_url = reverse('main:volonter')
        self.projects_url = reverse('main:projekt')
        self.volonter_create_url = reverse('main:join')
        self.skupine_url = reverse('main:skupina')
        self.crud_url = reverse('main:crud')
        self.volonter_update_url = reverse('main:updatevolonter', args=[1])  # volonter s ID-om 1
        self.volonter_delete_url = reverse('main:deletevolonter', args=[1]) 
        self.project_create_url = reverse('main:addprojekt')
        self.project_update_url = reverse('main:updateprojekt', args=[1])  # projekt s ID-om 1
        self.skupina_create_url = reverse('main:addskupina')
        self.skupina_update_url = reverse('main:updateskupina', args=[1])  # skupina with ID 1
        self.skupina_delete_url = reverse('main:deleteskupina', args=[1])  # skupina with ID 1

        # Stvaranje testnih korisnika za autentikaciju
        self.user = User.objects.create_user(username='test_user', password='12345')

    def test_volonter_list_GET(self):
        response = self.client.get(self.volonters_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'volonteri.html')

    def test_project_list_GET(self):
        response = self.client.get(self.projects_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projekti_list.html')

    def test_volonter_create_GET(self):
        self.client.login(username='test_user', password='12345')
        response = self.client.get(self.volonter_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'join.html')

    def test_crud_GET(self):
        self.client.login(username='test_user', password='12345')
        response = self.client.get(self.crud_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'crud.html')

    def test_volonter_update_GET(self):
        self.client.login(username='test_user', password='12345')

        projekt = Projekt.objects.create(naziv='Testni projekt', datum_projekta=date.today(), mjesto='Testno mjesto', opis='Opis testnog projekta')
        volonter = Volonter.objects.create(ime='Test', prezime='Volonter', godine=30, volonter_prije=True, projekt=projekt)
        url = reverse('main:updatevolonter', args=[volonter.pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_volonter.html')

    def test_volonter_delete_GET(self):
        self.client.login(username='test_user', password='12345')

        projekt = Projekt.objects.create(naziv='Test projekta', datum_projekta=date.today(), mjesto='Testno mjesto', opis='Opis testnog projekta')
        volonter = Volonter.objects.create(ime='Test', prezime='Volonter', godine=30, volonter_prije=True, projekt=projekt)
        url = reverse('main:deletevolonter', args=[volonter.pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_volonter.html')

    def test_project_create_GET(self):
        self.client.login(username='test_user', password='12345')
        response = self.client.get(self.project_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_projekt.html')

    def test_project_update_GET(self):
        self.client.login(username='test_user', password='12345')

        project = Projekt.objects.create(naziv='Test projekt', datum_projekta= date.today(), opis='Testni opis')
        url = reverse('main:updateprojekt', args=[project.pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_projekt.html')

    def test_skupina_list_GET(self):
        response = self.client.get(self.skupine_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'skupine.html')

    def test_skupina_create_GET(self):
        self.client.login(username='test_user', password='12345')
        response = self.client.get(self.skupina_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_skupina.html')

    def test_skupina_update_GET(self):
        self.client.login(username='test_user', password='12345')

        skupina = Volonterska_skupina.objects.create(naziv='Testna skupina')
        url = reverse('main:updateskupina', args=[skupina.pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_skupina.html')

    def test_skupina_delete_GET(self):
        self.client.login(username='test_user', password='12345')

        skupina = Volonterska_skupina.objects.create(naziv='Testna skupina')
        url = reverse('main:deleteskupina', args=[skupina.pk])
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_skupina.html')