<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-01-13 07:15
=======
# Generated by Django 4.0.1 on 2022-01-13 09:14
>>>>>>> patient_model

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
<<<<<<< HEAD
            field=models.DateField(default=datetime.datetime(2022, 1, 13, 7, 15, 54, 897375)),
=======
            field=models.DateField(default=datetime.datetime(2022, 1, 13, 9, 14, 17, 204503)),
>>>>>>> patient_model
        ),
    ]