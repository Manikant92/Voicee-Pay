# Generated by Django 3.2.12 on 2022-04-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(default='1240-3851-0370-9480', max_length=19, unique=True),
        ),
    ]
