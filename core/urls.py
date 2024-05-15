from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('historico', views.historico, name='historico'),
]
