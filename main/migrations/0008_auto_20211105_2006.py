# Generated by Django 3.2.8 on 2021-11-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_property_floors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='balcony',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathroom',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedroom',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]