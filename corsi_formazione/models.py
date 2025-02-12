from django.db import models
from datetime import datetime
# Create your models here.

class Corso(models.Model):
    titolo = models.CharField(max_length=30)
    descrizione = models.TextField(max_length=40)
    data_inizio = models.DateField(blank=True)
    data_fine = models.DateField(blank=True)
    posti_disponibili = models.IntegerField(blank=True)
    
    
    def __str__(self):
        return self.titolo + " " + self.descrizione
    
    class Meta:
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"