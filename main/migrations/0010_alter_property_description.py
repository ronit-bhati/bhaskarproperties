# Generated by Django 3.2.8 on 2023-04-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211207_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=3500),
        ),
    ]
