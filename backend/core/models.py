from django.db import models
from localflavor.br.br_states import STATE_CHOICES

class Endereco(models.Model):
    endereco = models.CharField('Endereço', max_length=100, null=True, blank=True)

    complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)

    bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)

    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)

    uf = models.CharField('UF', max_length=100, choices=STATE_CHOICES, null=True, blank=True)

    cep = models.CharField('CEP', max_length=100, null=True, blank=True)

    class Meta:
        abstract = True