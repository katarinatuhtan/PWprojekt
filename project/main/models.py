from django.db import models

class Projekt(models.Model):
    naziv = models.CharField(max_length=30)
    datum_projekta = models.DateField()
    mjesto=models.CharField(max_length=30, default=" ")
    opis = models.TextField()

    def __str__(self):
        return self.naziv
    
class Volonter(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    godine=models.IntegerField(default=0)
    volonter_prije=models.BooleanField(default=True)
    projekt=models.ForeignKey(Projekt, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime

class Volonterska_skupina(models.Model):
    naziv = models.CharField(max_length=30)
    volonteri = models.ManyToManyField('Volonter', related_name='volonterske_skupine')

    def __str__(self):
        return self.naziv
