from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('NomeCli', 'Bebida', 'Acompanhamento', 'StatusPedido', 'DataPed')
    list_filter = ('StatusPedido', 'DataPed')
    search_fields = ('StatusPedido', 'DataPed')
