# Generated by Django 2.2.1 on 2019-05-20 18:00

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
                ('client_id', models.AutoField(help_text='unique id of a client.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='the client name.', max_length=100)),
                ('surname', models.CharField(help_text='the client surname.', max_length=100)),
                ('email', models.EmailField(help_text='the client email.', max_length=254)),
                ('telephone', models.CharField(help_text='the client telephone.', max_length=11)),
                ('cpf', models.CharField(help_text='the client identification.', max_length=11, unique=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
