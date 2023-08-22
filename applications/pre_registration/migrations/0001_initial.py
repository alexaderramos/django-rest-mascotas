# Generated by Django 4.1.1 on 2023-08-18 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('consultation', models.TextField()),
                ('pet_name', models.CharField(max_length=255)),
                ('pet_specie', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pre registro',
                'verbose_name_plural': 'Pre registros',
            },
        ),
    ]