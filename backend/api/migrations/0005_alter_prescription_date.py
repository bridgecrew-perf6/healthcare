# Generated by Django 4.0.1 on 2022-01-13 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 13, 9, 16, 5, 465657)),
        ),
    ]
