# Generated by Django 4.1.1 on 2023-08-19 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]