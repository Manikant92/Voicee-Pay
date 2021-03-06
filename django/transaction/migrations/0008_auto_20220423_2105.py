# Generated by Django 3.2.12 on 2022-04-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_auto_20220416_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.CharField(default='1883-1708-6568-9844', max_length=19, unique=True),
        ),
    ]
