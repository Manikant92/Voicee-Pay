# Generated by Django 3.2.12 on 2022-04-16 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_alter_bankaccount_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='receiver_name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender_name',
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='receiver_account', to='transaction.customer'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender_account', to='transaction.customer'),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(default='1029-1417-7045-8613', max_length=19, unique=True),
        ),
    ]