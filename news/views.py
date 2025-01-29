from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista 
import datetime





def queryBase(request):
    #1.Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome = Articolo.objects.filter(giornalista__cognome='Bianchi')
    #2. Totale
    numero_totale_articoli = Articolo.objects.count()

    #3.Contare il numero di articoli scritti da un giornalista specifico:
    giornalista_1 = Giornalista.objects.get(id=2)
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()

    #4.Ordinare gli articoli per numero di visualizzazioni in ordine decrescente:
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')

    #5.tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #6.articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()

    #7.Tutti i giornalisti nati dopo una certa data:
    giornalisti_data = Giornalista.objects.filter(nascita=datetime.date(1990, 1, 1))

    #8.tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno =Articolo.objects.filter(data=datetime.date(2023, 1, 1))

    #9.tutti gli articoli pubblicati in un intervallo di date
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

    #10.gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati = Giornalista.objects.filter(nascita=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    #11.il giornalista più giovane:
    giornalista_giovane = Giornalista.objects.order_by('nascita').first()

    #12.il giornalista più anziano:
    giornalista_anziano = Giornalista.objects.order_by('-nascita').first()

    #13. gli ultimi 5 articoli pubblicati:
    ultimi = Articolo.objects.order_by('-data')[:5]

    #14. tutti gli articoli con un certo numero minimo di visualizzazioni:
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #15. tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')
    # Creare il dizionario context
    context = {
    'articoli_cognome': articoli_cognome,
    'numero totale articoli':numero_totale_articoli,
    }
    
    #16 Articoli pubblicati in un certo mese di un anno specifico:
    #nota per poter modificare la data di un articolo togliere la proprietà auto_now=True al field data nel model
        #poi dare i comandi makemigrations e migrate per applicare le modifiche al database
        
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)

     #17 Giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()

    """
    spiegazione dettagliata:
        Giornalista.objects: Inizia dalla classe del modello Giornalista.
        .filter(articoli_visualizzazioni_gte=100): Utilizza il metodo filter() per filtrare i giornalisti
        in base al campo visualizzazioni nel modello Articolo. La notazione articoli_visualizzazioni indica
        che si sta seguendo la relazione inversa dalla classe Giornalista alla classe Articolo attraverso
        il campo ForeignKey giornalista nel modello Articolo.
        .distinct(): E' un metodo assicura che i risultati siano distinti, eliminando eventuali duplicati.
        In questo caso, ciò è utile perché un giornalista potrebbe essere associato a più articoli che soddisfano
        il criterio, e vogliamo ottenere solo una volta ogni giornalista che ha scritto almeno un articolo popolare.
        """
        #UTILIZZO DI PIU' CONDIZIONI DI SELEZIONE
    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
        # Per mettere in AND le condizioni separarle con la virgola
        # 18 ... scrivi quali articoli vengono selezionati
    articoli_con_and = Articolo.objects.filter(giornalista__nascita__gt=data, visualizzazioni__gte=visualizzazioni)

        # Per mettere in OR le condizioni utilizzare l'operatore Q
    from django.db.models import Q
        # 19 ... scrivi quali articoli vengono selezionati
    articoli_con_or = Articolo.objects.filter(Q(giornalista__nascita__gt=data) | Q(visualizzazioni__lte=visualizzazioni))

        # Per il NOT (~) utilizzare l'operatore Q
        #20 ... scrivi quali articoli vengono selezionati
    articoli_con_not = Articolo.objects.filter(~Q(giornalista__nascita__lt=data))
        #oppure il metodo exclude
        # ... spiegala
    articoli_con_not = Articolo.objects.exclude(giornalista__nascita__lt=data)








def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(a) + "<br>" + str(g)
    
    return HttpResponse("<h1>"+ response+"</h1>")

def articoloDetailView(request,pk=None):
    articolo = get_object_or_404(Articolo,pk=pk)
    context = {"articolo":articolo}
    return render(request,"articolo_detail.html",context)

def listaArticoli(request, pk=None):
    if pk==None:
        articoli = Articolo.objects.all()
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
    context = {
        'articoli':articoli,
    }
    return render(request,'lista_articoli.html',context)
    