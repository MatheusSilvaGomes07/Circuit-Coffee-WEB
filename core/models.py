from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    NomeCli = models.CharField(max_length=72, null=True)
    Bebida = models.CharField(max_length=72, null=True)
    Acompanhamento = models.CharField(max_length=72)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = (
        ('Aprovado', 'APROVADO'),
        ('Cancelado', 'CANCELADO'),
        ('Aguardando pagamento', 'PAGAMENTO'),
    )
    StatusPedido = models.CharField(max_length=72, choices=STATUS, null=True)
    DataPed = models.DateField(auto_now_add=True, null=True)
    ObsPed = models.CharField(max_length=72, null=True)
