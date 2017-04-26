import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone

# Create your models here.
class Lancamentos(models.Model):
    lancamentosId = models.AutoField(primary_key=True)
    tipoLancamento = models.CharField(max_length=1)
    numeroDocumento = models.CharField(max_length=20)
    dataVencimento = models.DateField()
    dataEmissao = models.DateField()
    valorTitulo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")

class baixas(models.Model):
    baixasId = models.AutoField(primary_key=True)
    lancamentosId = models.ForeignKey(Lancamentos,"lancamentosId")
