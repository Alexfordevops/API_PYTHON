from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins #
from rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView #
from rest_framework_simplejwt.tokens import RefreshToken #

# Trata as requisições do cliente com generic_views (API V1)

# Requisições de indivíduo
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Requisições de coleção
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Requisições de indivíduo
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # Retorna um obejto
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
    
# Requisições de coleção
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    # Retorna vários objetos
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
# API V2 com View_set

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Autenticação do usuário / #IsAuthenticated

    # Avaliações por curso
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)
    
    # Avaliação específica por curso
    @action(detail=True, methods=['get'], url_path='avaliacoes/(?P<avaliacao_pk>[^/.]+)')
    def avaliacao(self, request, pk=None, avaliacao_pk=None):
        curso = self.get_object()
        avaliacao = get_object_or_404(curso.avaliacoes.all(), pk=avaliacao_pk)
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)
    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Autenticação do usuário / #IsAuthenticated

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=205)
        except Exception as e:
            return Response(status=400, data={"error": str(e)})
