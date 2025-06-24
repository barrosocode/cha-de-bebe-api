from rest_framework import serializers
from app import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# ============================================================
# =====================User Serializer========================
# ============================================================

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Definindo o campo 'password' explicitamente
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    # Mude este campo para permitir escrita e leitura de nomes de grupo
    groups = serializers.SlugRelatedField(
        queryset=Group.objects.all(),
        many=True,
        slug_field='name',
        required=False,
        allow_empty=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'groups', 'password')

    # Sobrescreva o método create para lidar com o hashing da senha
    def create(self, validated_data):
        # Use o manager padrão do User nativo para criar o usuário
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''), # Email pode ser opcional
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_staff=validated_data.get('is_staff', False),
            is_active=validated_data.get('is_active', True)
        )

        user.groups.set(validated_data.get('groups', []))

        return user

    # Sobrescreva o método update para lidar com a atualização da senha
    def update(self, instance, validated_data):
        # Se a senha for fornecida, hash ela
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')

        # Atualiza os outros campos
        return super().update(instance, validated_data)

# ============================================================
# ===================Convidado Serializer=====================
# ============================================================

class ConvidadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Convidado
        fields = '__all__'

# ============================================================
# ===================Mensagem Serializer======================
# ============================================================

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensagem
        fields = '__all__'

# ============================================================
# ====================Tamanho Serializer======================
# ============================================================

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tamanho
        fields = '__all__'

# ============================================================
# ====================Fralda Serializer=======================
# ============================================================

class FraldaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fralda
        fields = '__all__'

# ============================================================
# ===============Fralda_Convidado Serializer==================
# ============================================================

class Fralda_ConvidadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fralda_Convidado
        fields = '__all__'

# ============================================================
# ===================Presente Serializer======================
# ============================================================

class PresenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presente
        fields = '__all__'

# ============================================================
# ==============Presente_Convidado Serializer=================
# ============================================================

class Presente_ConvidadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presente_Convidado
        fields = '__all__'
