# Generated by Django 5.0.3 on 2024-04-24 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0017_remove_course_year_taught'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year_taught',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning_system.year'),
            preserve_default=False,
        ),
    ]