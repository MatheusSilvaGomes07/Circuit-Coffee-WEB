from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from core.forms import PedidoForm
from .models import Pedido
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



@login_required
def index(request):
    pedidos_aguardando_pagamento = Pedido.objects.filter(StatusPedido__in=['Aguardando'])

    return render(request, 'index.html', {'pedido': pedidos_aguardando_pagamento})

@login_required
def historico(request):
    pedidos_pagos_cancelados = Pedido.objects.filter(StatusPedido__in=['Cancelado', 'Aprovado'])

    return render(request, 'historico.html', {'pedido':pedidos_pagos_cancelados})

@login_required
def pagos(request):
    pedidos_pagos = Pedido.objects.filter(StatusPedido__in=['Aprovado'])

    return render(request, 'pedpagos.html', {'pedido':pedidos_pagos})

@login_required
def cancelados(request):
    pedidos_cancelados = Pedido.objects.filter(StatusPedido__in=['Cancelado'])

    return render(request, 'pedcancelados.html', {'pedido':pedidos_cancelados})

@require_POST
@login_required
def adicionar_pedido(request):
    form = PedidoForm(request.POST)
    if form.is_valid():
        pedido = form.save()
        return JsonResponse({'success': True, 'pedido_id': pedido.id})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})

@login_required
def deletar_pedido(request, pedido_id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=pedido_id)
        pedido.delete()
        return redirect('index')
    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)

@login_required
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