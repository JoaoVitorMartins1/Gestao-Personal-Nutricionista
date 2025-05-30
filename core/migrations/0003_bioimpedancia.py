# Generated by Django 5.1.7 on 2025-04-01 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_aluno_data_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bioimpedancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_medicao', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('pct_gordura', models.DecimalField(decimal_places=1, max_digits=4)),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coxa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('panturrilha', models.DecimalField(decimal_places=2, max_digits=5)),
                ('braco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='core.aluno')),
            ],
        ),
    ]
