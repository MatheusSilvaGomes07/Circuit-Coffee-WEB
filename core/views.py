from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import Pedido

def index(request):
    pedidos_aguardando_pagamento = Pedido.objects.filter(StatusPedido__in=['Aguardando pagamento'])

    return render(request, 'index.html', {'pedido': pedidos_aguardando_pagamento})

def historico(request):
    pedidos_pagos_cancelados = Pedido.objects.filter(StatusPedido__in=['Cancelado', 'Aprovado'])

    return render(request, 'historico.html', {'pedido':pedidos_pagos_cancelados})

# views.py

def alterar_status(request, pedido_id):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        if not novo_status:
            return HttpResponseBadRequest('Um novo status deve ser selecionado.')
        
        
        status_validos = ['Aprovado', 'Cancelado', 'Aguardando pagamento']
        if novo_status not in status_validos:
            return HttpResponseBadRequest('O status selecionado não é válido.')
        
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.StatusPedido = novo_status
        pedido.save()
    return redirect('index')