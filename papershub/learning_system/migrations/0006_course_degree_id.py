# Generated by Django 5.0.3 on 2024-04-03 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0005_degree_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='degree_id',
            field=models.ForeignKey(default='CEIT', on_delete=django.db.models.deletion.CASCADE, to='learning_system.degree_program'),
            preserve_default=False,
        ),
    ]