# Generated by Django 3.2.9 on 2021-11-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_empresa_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='observacao',
            field=models.TextField(blank=True),
        ),
    ]