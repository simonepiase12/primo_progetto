from django.shortcuts  import get_object_or_404,redirect, render

from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required
from .forms import FormContatto
from .models import Contatto
from django.http import HttpResponse

# Create your views here.
def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        
        if form.is_valid():
            print("Il form è valido")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])
            
            print("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
        
        
    else:
        form = FormContatto()
            
    context = {"form": form}
    return render(request, "contatto.html",context)

def lista(request):
    contatti = Contatto.objects.all()
    context = {
        'contatti':contatti,
    }
    return render(request,'lista_contatti.html',context)



@login_required(login_url="/accounts/login")
def modifica_contatto(request, pk):
    # preleva dal database l'oggetto la cui chiave primaria è passata come parametro
    contatto = get_object_or_404(Contatto, id=pk)


    if request.method == "GET": #prima chiamata get per caricare il form
        form = FormContatto(instance=contatto) #al construttore del form passo il contatto prelevato dal db
    if request.method == "POST": #seconda chiamata post per modificare il contatto
        form = FormContatto(request.POST, instance=contatto) #ora passo oltre al contatto prelevato dal db anche i dati modificati
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista') # url che reindirizza alla pagina lista_contatti.html

    context={'form': form, 'contatto': contatto}
    return render(request, 'modifica_contatto.html', context)


    

@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST": # vuol dire che l'utente ha inviato il form che conferma l'eliminazione
        contatto.delete() #elimina il contatto dal database
        return redirect('forms_app:lista')
    context= {'contatto': contatto}
    return render(request,'elimina_contatto.html',context)