# Generated by Django 3.2 on 2021-08-07 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210807_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='type',
        ),
        migrations.DeleteModel(
            name='BookingInfo',
        ),
    ]