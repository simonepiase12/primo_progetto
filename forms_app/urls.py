from django.urls import path
from .views import contatti,lista,modifica_contatto,elimina_contatto

app_name = "forms_app"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('lista', lista, name='lista'),
    path('elimina_contatto/<int:pk>', elimina_contatto, name='elimina_contatto'),
    path('modifica_contatto/<int:pk>', modifica_contatto, name='modifica_contatto'),

]