# Generated by Django 5.0.6 on 2024-06-24 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0004_alter_ordemservicoitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservicoitem',
            name='ordem_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_servico_itens', to='servico.ordemservico', verbose_name='ordem de servico'),
        ),
    ]
