from django import forms
from .models import Pedido
from allauth.account.forms import LoginForm

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['NomeCli', 'Bebida', 'Acompanhamento', 'Valor', 'StatusPedido', 'ObsPed']
        

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})