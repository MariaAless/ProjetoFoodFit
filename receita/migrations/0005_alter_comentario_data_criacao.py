# Generated by Django 4.2.5 on 2023-12-09 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0004_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
