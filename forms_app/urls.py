from django.urls import path
from .views import contatti,lista

app_name = "forms_app"

urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('lista', lista, name='lista'),
]