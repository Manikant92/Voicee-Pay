# Generated by Django 3.2.12 on 2022-04-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UssdSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.CharField(max_length=50)),
                ('user_phone', models.CharField(max_length=15)),
                ('user_input', models.TextField()),
            ],
        ),
    ]
