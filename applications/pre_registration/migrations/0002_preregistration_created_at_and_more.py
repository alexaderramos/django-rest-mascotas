# Generated by Django 4.1.1 on 2023-08-19 02:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pre_registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preregistration',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='preregistration',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='preregistration',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]