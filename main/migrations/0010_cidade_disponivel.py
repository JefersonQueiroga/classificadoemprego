# Generated by Django 3.2.9 on 2021-12-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_vaga_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
