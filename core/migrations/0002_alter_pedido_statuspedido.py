# Generated by Django 5.0.6 on 2024-05-15 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='StatusPedido',
            field=models.CharField(choices=[('Aprovado', 'APROVADO'), ('CANCELADO', 'CANCELADO'), ('Aguardando pagamento', 'PAGAMENTO')], max_length=72, null=True),
        ),
    ]