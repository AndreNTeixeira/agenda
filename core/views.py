from urllib import response

from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento


# Create your views here.

def retorna_local_evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(f"O local é {evento.local}")

#def index(request):
    return redirect('/agenda')


def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

