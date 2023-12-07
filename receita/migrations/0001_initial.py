# Generated by Django 4.2.5 on 2023-12-07 01:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='capa_receita')),
                ('nome', models.CharField(max_length=100)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('data_cadastro', models.DateField(default=datetime.date.today)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='receita.categoria')),
            ],
            options={
                'verbose_name': 'Receita',
            },
        ),
    ]
