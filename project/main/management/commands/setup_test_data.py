import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import (
    DogadajFactory,
    VolonterFactory,
    VolonterskaSkupinaFactory
)

NUM_PROJEKT = 10
NUM_VOLONTER = 150
NUM_SKUPINA= 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Projekt, Volonter, Volonterska_skupina]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PROJEKT):
            dogadaj = DogadajFactory()

        for _ in range(NUM_VOLONTER):
            volonter = VolonterFactory()
        
        for _ in range(NUM_SKUPINA):
            skupina = VolonterskaSkupinaFactory()