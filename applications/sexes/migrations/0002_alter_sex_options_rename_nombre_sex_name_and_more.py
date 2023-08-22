# Generated by Django 4.1.1 on 2023-08-20 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sexes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sex',
            options={'verbose_name': 'Sexo', 'verbose_name_plural': 'Sexos'},
        ),
        migrations.RenameField(
            model_name='sex',
            old_name='nombre',
            new_name='name',
        ),
        migrations.AddField(
            model_name='sex',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sex',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]