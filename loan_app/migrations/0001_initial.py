# Generated by Django 2.2.1 on 2019-05-20 18:00

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
                ('finished', models.BooleanField(default=False, verbose_name='Paid')),
                ('loan_id', models.CharField(blank=True, editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, help_text='loan amount in dollars.', max_digits=12)),
                ('term', models.DecimalField(decimal_places=0, help_text='number of months that will take until the loan gets paid-off.', max_digits=3)),
                ('rate', models.DecimalField(decimal_places=4, help_text='interest rate as decimal.', max_digits=4)),
                ('date', models.DateTimeField(help_text='when the loan was requested (origination date as an ISO 8601 string).')),
                ('instalment', models.DecimalField(blank=True, decimal_places=2, help_text='monthly loan payment.', max_digits=12)),
                ('_outstanding', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='outstanding')),
                ('_total_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='total value')),
                ('client_id', models.ForeignKey(default=None, help_text='unique id of a client. ', on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='clients.Client')),
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
                ('payment', models.CharField(choices=[('made', 'made'), ('missed', 'missed')], default='made', help_text='type of payment: made or missed.', max_length=6)),
                ('date', models.DateTimeField(help_text='payment date.')),
                ('amount', models.DecimalField(decimal_places=2, help_text='amount of the payment made or missed in dollars.', max_digits=8)),
                ('loan_id', models.ForeignKey(help_text='unique id of the loan.', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loan_app.Loan')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
