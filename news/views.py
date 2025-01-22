from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Giornalista 

def home(request):
    a=[]
    g=[]
    for art in Articolo.objects.all():
        a.append(art.titolo)
    
    for gio in Giornalista.objects.all():
        g.append(gio.nome)
    response = str(a) + "<br>" + str(g)
    
    return HttpResponse("<h1>"+ response+"</h1>")

def articoloDetailView(request,pk):
    articolo = get_object_or_404(Articolo,pk=pk)
    context = {"articolo":articolo}
    return render(request,"articolo_detail.html",context)
    