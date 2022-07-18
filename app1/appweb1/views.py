from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
from paciente.models import Paciente

def paginaprincipal(request):
    cantidad = Paciente.objects.count()
    pacientes = Paciente.objects.order_by('apellidos')
    mensaje = {'cantidad': cantidad, 'pacientes': pacientes}
    pagina = loader.get_template('paginaprincipal.html')
    #return HttpResponse(pagina.render())
    return HttpResponse(pagina.render(mensaje, request))