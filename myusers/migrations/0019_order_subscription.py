# Generated by Django 5.0.3 on 2024-05-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0018_remove_order_pending_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
    ]
