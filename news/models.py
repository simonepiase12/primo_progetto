
from django.db import models
from datetime import datetime

class Giornalista (models.Model):
    """il modello generico di un giornalista """
    nome = models.CharField(max_length=20) 
    cognome = models.CharField(max_length=20)
    nascita = models.DateField(blank=True,default=datetime.now())
    def _str__(self):
        return self.nome + " " + self.cognome
    
    class Meta:
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalisti"
        
class Articolo (models.Model):
    """ il modello generico di un articolo di news"""
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models. CASCADE, related_name="articoli")
    data = models.DateField(auto_now=True, blank=True)
    visualizzazioni = models.IntegerField(default=0,blank=True)
    
    def _str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"