from django.urls import path
from .views import index,lista

app_name = "corsi_formazione"

urlpatterns = [
       path('',index,name='home'),
       path('',lista,name='lista'),
]