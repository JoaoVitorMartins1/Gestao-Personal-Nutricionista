from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_personal = models.BooleanField(default=False)

    class Meta:
        db_table = 'core_user'  # Esta linha resolve o problema


class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)  # Isso substitui o id padrão
    telefone = models.CharField(max_length=20)
    nome = models.CharField(max_length=25)



    @property
    def id(self):
        return self.user_id  # Cria uma propriedade id que retorna user_id

    def __str__(self):
        return self.nome
class Aluno(models.Model):
    personal=models.ForeignKey(Personal, on_delete=models.CASCADE, related_name='alunos')
    nome=models.CharField(max_length=25,null=False, blank=False)
    data_nascimento=models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=True, blank=True)



class Bioimpedancia(models.Model):
    aluno=models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')
    data_medicao = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # em kg
    altura = models.DecimalField(max_digits=4, decimal_places=2)  # em metros
    pct_gordura = models.DecimalField(max_digits=4, decimal_places=1)  # 15.5%
    # Medidas corporais (em cm):
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    peito = models.DecimalField(max_digits=5, decimal_places=2)
    coxa = models.DecimalField(max_digits=5, decimal_places=2)
    panturrilha = models.DecimalField(max_digits=5, decimal_places=2)
    braco = models.DecimalField(max_digits=5, decimal_places=2)

class Plano(models.Model):
    STATUS_CHOICES=[
        ('ativo', 'ATIVO'),
        ('vencido', 'VENCIDO')

    ]
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name='plano')
    valor=models.DecimalField(max_digits=10,decimal_places=2)
    data_inicio=models.DateField(null=False, blank=False)
    data_vencimento=models.DateField(null=False, blank=False)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    def dias_restantes(self):
        from datetime import date
        return (self.data_vencimento-date.today()).days

class Dieta(models.Model):
    aluno=models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='dietas')
    data_criacao=models.DateField(auto_now_add=True)
    descricao=models.TextField()
