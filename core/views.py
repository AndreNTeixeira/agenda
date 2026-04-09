from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def retorna_local_evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(f"O local é {evento.local}")