from django.db import models
from backend.core.models import Endereco

class Cliente(Endereco):
    razao_social = models.CharField('Razão Social',max_length=120, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)

    class Meta:
        ordering = ('razao_social',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self) -> str:
        return f'{self.razao_social}'
    
