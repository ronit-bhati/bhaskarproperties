# Generated by Django 3.2.8 on 2023-04-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20230430_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.FloatField(),
        ),
    ]