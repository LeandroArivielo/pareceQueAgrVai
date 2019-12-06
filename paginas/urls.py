from django.urls import path
from .views import TrabalhoPageView, ONGsDeAnimaisPageView, ONGsDeAnimaisPedroIIPageView, VoluntariadoPageView, ListadeEventosPageView, oqEPageView
urlpatterns = [
    path('', TrabalhoPageView.as_view(), name ='trabalho'),
    path('ONGsDeAnimais', ONGsDeAnimaisPageView.as_view(), name ='ONGsDeAnimais'),
    path('ONGsDeAnimaisPedroII', ONGsDeAnimaisPedroIIPageView.as_view(), name ='ONGsDeAnimaisPedroII'),
    path('oqEVoluntariado', VoluntariadoPageView.as_view(), name ='Voluntariado'),
    path('ListadeEventos', ListadeEventosPageView.as_view(), name ='ListadeEventos'),
    path('oqE', oqEPageView.as_view(), name ='oqE'),
]