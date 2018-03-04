# Generated by Django 2.0.1 on 2018-02-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20180206_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
                ('body', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Event')),
            ],
        ),
    ]