# Generated by Django 4.1.1 on 2023-08-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_registration', '0002_preregistration_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preregistration',
            name='deleted_at',
        ),
        migrations.AddField(
            model_name='preregistration',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
