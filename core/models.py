from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    NomeCli = models.ForeignKey(User, on_delete=models.CASCADE)
    Bebida = models.CharField(max_length=72, null=True)
    Acompanhamento = models.CharField(max_length=72)
    STATUS = (
        ('Aprovado', 'APROVADO'),
        ('Cancelado', 'CANCELADO'),
        ('Aguardando pagamento', 'PAGAMENTO'),
        ('Concluido', 'CONCLUIDO')
    )
    StatusPedido = models.CharField(max_length=72, choices=STATUS, null=True)
    DataPed = models.DateField(auto_now_add=True, null=True)
