# Generated by Django 5.0.3 on 2024-04-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0020_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ManyToManyField(to='learning_system.semester'),
        ),
    ]