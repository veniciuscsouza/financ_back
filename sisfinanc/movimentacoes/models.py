import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
from cadastros import models

# Create your models here.
class Lancamentos(models.Model):
    lancamentosId = models.AutoField(primary_key=True)
    pessoaId = models.ForeignKey(cadastros.pessoaId)
    empresaId = models.ForeignKey(cadastros.empresaId)
    tipoLancamento = models.CharField(max_length=1)
    numeroDocumento = models.CharField(max_length=20)
    dataVencimento = models.DateField()
    dataEmissao = models.DateField()
    valorTitulo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")

class Baixas(models.Model):
    baixasId = models.AutoField(primary_key=True)
    formasPagamentoId = models.ForeignKey(FormasPagamento, "formasPagamentoId")
    empresaId = models.ForeignKey(Lancamentos, "lancamentosId")
    tipoLancamento = models.CharField(max_length=1)
    numeroDocumento = models.CharField(max_length=20)
    dataVencimento = models.DateField()
    dataEmissao = models.DateField()
    valorTitulo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")

class Tesouraria(models.Model):
    tesourariaId = models.AutoField(primary_key=True)
    formasPagamentoId = models.ForeignKey(FormasPagamento, "formasPagamentoId")
    empresaId = models.ForeignKey(Lancamentos, "lancamentosId")
    pessoaId = models.ForeignKey(cadastros.pessoaId)
    planoContasId = models.ForeignKey(cadastros.planoContasId)

class FormasPagamento(models.Model):
    formasPagamentoId = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50)
