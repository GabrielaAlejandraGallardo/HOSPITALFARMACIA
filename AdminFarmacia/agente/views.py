from django.shortcuts import render
from .models import Agente

# Create your views here.
def inicio(request):
    return render(request, 'pagina_base/inicio.html')

def lista_agentes(request):
    agentes = Agente.objects.all()
    return render(request, 'pagina_base/lista_agentes.html', {'agentes': agentes})

