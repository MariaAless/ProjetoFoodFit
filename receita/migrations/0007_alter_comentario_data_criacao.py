# Generated by Django 4.2.5 on 2023-12-09 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0006_alter_comentario_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]