# Generated by Django 4.1.1 on 2023-08-19 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_preregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='direction',
            new_name='address',
        ),
    ]