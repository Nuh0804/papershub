# Generated by Django 5.0.3 on 2024-05-05 07:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0015_order_transaction_id_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pending_status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='1234567890', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='placed_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='provider',
            field=models.CharField(choices=[('TIGO', 'Tigo'), ('VODACOM', 'Mpesa'), ('AIRTEL', 'Airtel'), ('HALOTEL', 'Halopesa'), ('AZAMPESA', 'Azampesa')], default='Tigo', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
