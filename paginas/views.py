from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class TrabalhoPageView(TemplateView):
    template_name = 'trabalho.html'

class ONGsDeAnimaisPageView(TemplateView):
    template_name = 'ONGsDeAnimais.html'

class ONGsDeAnimaisPedroIIPageView(TemplateView):
    template_name = 'ONGsDeAnimaisPedroII.html'

class VoluntariadoPageView(TemplateView):
    template_name = 'Voluntariado.html'

class ListadeEventosPageView(TemplateView):
    template_name = 'ListadeEventos.html'

class oqEPageView(TemplateView):
    template_name = 'oqE.html'