# Generated by Django 5.0.3 on 2024-05-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0019_order_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subscription',
        ),
        migrations.AddField(
            model_name='user',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
    ]