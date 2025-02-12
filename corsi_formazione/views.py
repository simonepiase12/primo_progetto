from django.shortcuts import render
from .models import Corso
from datetime import datetime
from django.http import HttpResponse
def lista(request):
   corsi_ordinati=Corso.objects.order_by('-data_inizio').first()
   
def view_c(request):
    corsi_filtrati = Corso.objects.filter(data__range=(datetime.date(2025, 5, 1), datetime.date(2030, 12, 31)))
    
def view_d(request):
    corsi_filtrati = Corso.objects.filter(Corso.posti_disponibili<20)

def view_e(request):
        corsi_filtrati = Corso.objects.filter(Corso.data_fine<=(datetime.date(2024,4,30)))

def index(request):
    a=[]
    for corso in Corso.objects.all():
        a.append(corso)
    response= str(a)
    return HttpResponse("<h1>"+ response+"</h1>")

def view_f(request):
    max=Corso.objects(0)
    min=Corso.objects(0)
    tot=0
    for corso in Corso.objects.all():
        if(corso.posti_disponibili>max):
            max=corso
        if(corso.posti_disponibili<min):
            min=corso
        tot+=corso.posti_disponibili
    print("Corso con più posti:",max.titolo)
    print("Corso con più posti:",min.titolo)
    print("posti disponibili:",tot)
            
    

    

