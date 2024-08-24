from django.urls import path
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#   VIEWS INICIO CUESTIONARIOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from .views import *
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#   VIEWS JSON INICIO CUESTIONARIOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from .json_response.json_view import *
urlpatterns = [
        path('inicio/', Inicio.as_view(), name='inicio'),
        path('cuestionario/<int:pk>/', Cuestionario_DetailView.as_view(), name='cuestionario'),
        # ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
        #  Rediccionamientos de petición asycrona
        # ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
        path('verificar_respuesta/', VerificarRespuestaView.as_view(), name='verificar_respuesta'),
        path('verificar_siguiente_pregunta/', VerificarSiguientePreguntaView.as_view(), name='verificar_siguiente_pregunta'),
        path('pregunta-cuestionario/<int:pk>/<int:cuestionario_id>/', PreguntaDetailView.as_view(), name='pregunta_cuestionario'),

    ]