from django.test import TestCase
from .models import Projekt, Volonter, Volonterska_skupina
from datetime import date

class TestModels(TestCase):

    #inicijalizacija podataka za testiranje
    def setUp(self):
        self.projekt1 = Projekt.objects.create(
            naziv='Projekt 1',
            datum_projekta=date(2024, 1, 1),
            mjesto='Mjesto 1',
            opis='Opis projekta 1'
        )

        self.volonter1 = Volonter.objects.create(
            ime='Ime 1',
            prezime='Prezime 1',
            godine=25,
            volonter_prije=True,
            projekt=self.projekt1
        )

        self.skupina1 = Volonterska_skupina.objects.create(
            naziv='Skupina 1'
        )
        self.skupina1.volonteri.add(self.volonter1)

    #test za projekte
    def test_projekt_model(self):
        self.assertEquals(self.projekt1.naziv, 'Projekt 1')
        self.assertEquals(self.projekt1.datum_projekta, date(2024, 1, 1))
        self.assertEquals(self.projekt1.mjesto, 'Mjesto 1')
        self.assertEquals(self.projekt1.opis, 'Opis projekta 1')


    #test za volontere
    def test_volonter_model(self):
        self.assertEquals(self.volonter1.ime, 'Ime 1')
        self.assertEquals(self.volonter1.prezime, 'Prezime 1')
        self.assertEquals(self.volonter1.godine, 25)
        self.assertTrue(self.volonter1.volonter_prije)
        self.assertEquals(self.volonter1.projekt, self.projekt1)


    #test za volonterske skupine
    def test_volonterska_skupina_model(self):
        self.assertEquals(self.skupina1.naziv, 'Skupina 1')
        self.assertEquals(self.skupina1.volonteri.first(), self.volonter1)
