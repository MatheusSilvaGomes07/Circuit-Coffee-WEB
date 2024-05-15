from django.http import JsonResponse
from django.shortcuts import render
from .models import Pedido

def index(request):
    pedidos_aguardando_pagamento = Pedido.objects.filter(StatusPedido__in=['Aguardando pagamento', 'Aprovado'])

    return render(request, 'index.html', {'pedido': pedidos_aguardando_pagamento})

def historico(request):
    pedidos_pagos_cancelados = Pedido.objects.filter(StatusPedido__in=['Concluido', 'Cancelado'])

    return render(request, 'historico.html', {'pedido':pedidos_pagos_cancelados})