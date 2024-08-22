from django.urls import path
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#   MODELO INICIO CUESTIONARIOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from .views import *
urlpatterns = [
        path('inicio/', Inicio.as_view(), name='inicio'),
        path('cuestionario/<int:pk>/', Cuestionario_DetailView.as_view(), name='cuestionario'),

    ]