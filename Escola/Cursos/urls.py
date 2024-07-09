from django.urls import path
from .views import CursosAPIView, AvaliacoesAPIView, CursoAPIView, AvaliacaoAPIView, CursoViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

# Criação das rotas locais da aplicação Cursos

# Rotas automáticas com Routers (API V2)
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

# Rotas manuais (API V1)
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'), # Todos os cursos
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='cursos'), # Cursos por id
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'), # avaliacoes de determinado curso
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'), # determinada avaliacao de determinado curso
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'), # Todas as avaliações
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='Avaliacao'), # Determinada avaliação
]
urlpatterns += router.urls # Acoplamento dos rotas router + urlpatterns

