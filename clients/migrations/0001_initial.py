# Generated by Django 2.2.1 on 2019-05-14 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
