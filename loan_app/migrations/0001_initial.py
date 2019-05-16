# Generated by Django 2.2.1 on 2019-05-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('finished', models.BooleanField(default=False, verbose_name='Payed')),
                ('loan_id', models.CharField(blank=True, editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('term', models.DecimalField(decimal_places=0, max_digits=3)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=4)),
                ('date', models.DateTimeField()),
                ('instalment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('_outstanding', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='outstanding')),
                ('client_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='clients.Client')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.CharField(choices=[('made', 'made'), ('missed', 'missed')], default='made', max_length=2)),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loan_app.Loan')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
