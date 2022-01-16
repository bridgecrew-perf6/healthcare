# Generated by Django 4.0.1 on 2022-01-16 14:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=30)),
                ('patient_name', models.CharField(max_length=30)),
                ('examination', models.TextField()),
                ('investigation', models.TextField()),
                ('diagnosis', models.TextField()),
                ('advice', models.TextField()),
                ('comment', models.TextField()),
                ('chief_complain', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField(default=datetime.date(2022, 1, 16))),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_item', models.CharField(max_length=30)),
                ('strength', models.CharField(max_length=20)),
                ('preparation', models.CharField(max_length=20)),
                ('route', models.CharField(max_length=20)),
                ('dose', models.CharField(max_length=20)),
                ('direction', models.CharField(max_length=20)),
                ('frequency', models.CharField(max_length=60)),
                ('duration', models.CharField(max_length=30)),
                ('total_quantity', models.IntegerField()),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eprescription.prescription')),
            ],
        ),
    ]
