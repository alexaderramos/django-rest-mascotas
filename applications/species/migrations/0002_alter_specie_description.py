# Generated by Django 4.1.1 on 2023-08-19 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specie',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]