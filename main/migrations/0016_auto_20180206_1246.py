# Generated by Django 2.0.1 on 2018-02-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180201_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cult',
            name='slug',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
