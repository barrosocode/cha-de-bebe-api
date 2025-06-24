from rest_framework import viewsets
from app.api import serializers
from app import models
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

# ============================================================
# ======================User ViewSet==========================
# ============================================================

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# ====================Convidado ViewSet=======================
# ============================================================

class ConvidadoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ConvidadoSerializer
    queryset = models.Convidado.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# ====================Mensagem ViewSet========================
# ============================================================

class MensagemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MensagemSerializer
    queryset = models.Mensagem.objects.all()

    # Configuração das permissões
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# =====================Tamanho ViewSet========================
# ============================================================

class TamanhoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TamanhoSerializer
    queryset = models.Tamanho.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

# ============================================================
# =====================Fralda ViewSet=========================
# ============================================================

class FraldaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FraldaSerializer
    queryset = models.Fralda.objects.all()

    # Configurações de permissões
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# ================Fralda_Convidado ViewSet====================
# ============================================================

class Fralda_ConvidadoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Fralda_ConvidadoSerializer
    queryset = models.Fralda_Convidado.objects.all()

    # Configurações de permissões
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# ====================Presente ViewSet========================
# ============================================================

class PresenteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PresenteSerializer
    queryset = models.Presente.objects.all()

    # Configurações de permissão
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()

# ============================================================
# ===============Presente_Convidado ViewSet===================
# ============================================================

class Presente_ConvidadoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Presente_ConvidadoSerializer
    queryset = models.Presente_Convidado.objects.all()

    # Configurações de permissões
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return super().get_permissions()
