# Generated by Django 4.0.1 on 2022-01-14 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eprescription', '0002_alter_medication_duration_alter_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='duration',
            field=models.DateField(default=datetime.datetime(2022, 1, 14, 11, 47, 10, 185984)),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 14, 11, 47, 10, 185564)),
        ),
    ]