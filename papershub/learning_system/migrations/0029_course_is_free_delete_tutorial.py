# Generated by Django 5.0.3 on 2024-05-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0028_rename_course_id_pastpaper_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
