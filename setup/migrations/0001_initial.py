# Generated by Django 3.2.14 on 2022-07-28 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Location ID')),
                ('location_name', models.CharField(max_length=255, verbose_name='Location Name')),
            ],
        ),
    ]
