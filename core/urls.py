from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('historico', views.historico, name='historico'),
    path('alterar_status/<int:pedido_id>/', views.alterar_status, name='alterar_status'),
    path('pedpagos', views.pagos, name='pedpagos'),
    path('pedcancelados', views.cancelados, name='pedcancelados'),
]
