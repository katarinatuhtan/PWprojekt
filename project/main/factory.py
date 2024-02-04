import factory
from factory.django import DjangoModelFactory
from factory import fuzzy
from datetime import datetime, timedelta

from main.models import *

class ProjektFactory(DjangoModelFactory):
    class Meta:
        model=Projekt
    #naziv = factory.Faker("first_name")
    @factory.sequence
    def naziv(n):
        return f"Projekt {n + 1}"
    
    #datum_projekta = factory.Faker("date_time")
    @factory.lazy_attribute
    def datum_projekta(self):
        return datetime.now() + timedelta(days=30)

    mjesto = factory.Faker("city")
    opis = factory.Faker("sentence", nb_words=50)

class VolonterFactory(DjangoModelFactory):
    class Meta:
        model=Volonter
    ime=factory.Faker("first_name")
    prezime=factory.Faker("last_name")
    godine = factory.LazyAttribute(lambda x: fuzzy.FuzzyInteger(13, 80).fuzz())
    volonter_prije=factory.Faker("boolean")
    projekt=factory.Iterator(Projekt.objects.all())

class VolonterskaSkupinaFactory(DjangoModelFactory):
    class Meta:
        model = Volonterska_skupina

    #naziv = factory.Faker("first_name")
    @factory.sequence
    def naziv(n):
        return f"Skupina {n + 1}"
    
    @factory.post_generation
    def volonteri(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.volonteri.add(*extracted)