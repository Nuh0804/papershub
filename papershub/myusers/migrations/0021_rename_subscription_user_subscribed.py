# Generated by Django 5.0.3 on 2024-05-09 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0020_remove_order_subscription_user_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='subscription',
            new_name='subscribed',
        ),
    ]
