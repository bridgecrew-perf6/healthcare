# Generated by Django 4.0.1 on 2022-01-13 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 13, 16, 25, 37, 624090)),
        ),
    ]
