from django.db import models
from django.contrib.auth.hashers import make_password

# ============================================================
# ======================Model UserType========================
# ============================================================

class UserType(models.Model):
    # fields
    name = models.CharField(max_length=True, max_length=20, null=False)

# ============================================================
# ========================Model User==========================
# ============================================================

class User(models.Model):
    # fields
    name = models.CharField(unique=True, max_length=100, null=False)
    login = models.CharField(unique=True, max_length=20, null=False)
    password = models.CharField(max_length=128, null=False)

    # relationships
    id_type = models.ForeignKey(UserType, on_delete=models.CASCADE)

    # functions
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


# ============================================================
# =====================Model Convidado========================
# ============================================================

class Convidado(models.Model):
    # fields
    name = models.CharField(unique=True, max_length=50, null=False)
    confirmed = models.BooleanField(null=False, default=False)

# ============================================================
# =====================Model Mensagens========================
# ============================================================

class Mensagem(models.Model):
    # fields
    convidado = models.CharField(max_length=50, null=False)
    mensagem = models.TextField(null=False)

# ============================================================
# =====================Model Tamanhos=========================
# ============================================================

class Tamanho(models.Model):
    # fields
    name = models.CharField(max_length=1, null=False, unique=True)

# ============================================================
# ======================Model Fraldas=========================
# ============================================================

class Fralda(models.Model):
    # fields
    quantidade = models.IntegerField(null=False, default=1)
    status = models.BooleanField(null=False, default=True)

    # relationships
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)

# ============================================================
# ==================Model Fralda_convidado====================
# ============================================================

class Fralda_Convidado(models.Model):
    # relationships
    id_convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE)
    id_fralda = models.ForeignKey(Fralda, on_delete=models.CASCADE)

# ============================================================
# =====================Model Presentes========================
# ============================================================

class Presente(models.Model):
    # fields
    name = models.CharField(unique=True, max_length=50, null=False)
    descricao = models.TextField(null=False)
    imagem = models.ImageField(upload_to='presentes/', null=True)
    link = models.CharField(max_length=350, null=False)
    quantidade = models.IntegerField(null=False, default=1)
    status = models.BooleanField(null=False, default=True)

# ============================================================
# ================Model Presente_convidado====================
# ============================================================

class Presente_Convidado(models.Model):
    # relationships
    id_convidado = models.ForeignKey(Convidado, on_delete=models.CASCADE)
    id_presente = models.ForeignKey(Presente, on_delete=models.CASCADE)
