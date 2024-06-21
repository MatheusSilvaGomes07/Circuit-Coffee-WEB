from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm

def index(request):
    pedidos_aguardando_pagamento = Pedido.objects.filter(StatusPedido__in=['Aguardando'])

    return render(request, 'index.html', {'pedido': pedidos_aguardando_pagamento})

def historico(request):
    pedidos_pagos_cancelados = Pedido.objects.filter(StatusPedido__in=['Cancelado', 'Aprovado'])

    return render(request, 'historico.html', {'pedido':pedidos_pagos_cancelados})

def pagos(request):
    pedidos_pagos = Pedido.objects.filter(StatusPedido__in=['Aprovado'])

    return render(request, 'pedpagos.html', {'pedido':pedidos_pagos})

def cancelados(request):
    pedidos_cancelados = Pedido.objects.filter(StatusPedido__in=['Cancelado'])

    return render(request, 'pedcancelados.html', {'pedido':pedidos_cancelados})

def alterar_status(request, pedido_id):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
        if not novo_status:
            return HttpResponseBadRequest('Um novo status deve ser selecionado.')
        
        
        status_validos = ['Aprovado', 'Cancelado', 'Aguardando']
        if novo_status not in status_validos:
            return HttpResponseBadRequest('O status selecionado não é válido.')
        
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.StatusPedido = novo_status
        pedido.save()
    return redirect('index')

def adicionar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PedidoForm()
    return render(request, 'adicionar_pedido.html', {'form': form})

def deletar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('index')
    return render(request, 'deletar_pedido.html', {'pedido': pedido})