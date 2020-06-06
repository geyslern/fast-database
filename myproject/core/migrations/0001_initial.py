# Generated by Django 2.2.13 on 2020-06-06 06:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='título')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantidade')),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'compra',
                'verbose_name_plural': 'compras',
            },
        ),
    ]
