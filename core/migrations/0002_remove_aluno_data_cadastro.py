# Generated by Django 5.1.7 on 2025-04-01 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='data_cadastro',
        ),
    ]
