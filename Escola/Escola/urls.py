from django.contrib import admin
from django.urls import path, include
from Cursos.urls import router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

from Cursos.views import LogoutView #

# Rotas globais do projeto

urlpatterns = [
    path('api/v1/', include('Cursos.urls')), # API V1 
    path('api/v2/', include('Cursos.urls')), # API V2 <- release
    path('admin/', admin.site.urls),
    path('auth', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Receber token de autenticação
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Atualizar token de autenticação
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/logout/', LogoutView.as_view(), name='auth_logout'),
]
