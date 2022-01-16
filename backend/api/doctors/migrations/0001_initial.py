# Generated by Django 4.0.1 on 2022-01-16 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstname', models.CharField(default='', max_length=40)),
                ('lastname', models.CharField(default='', max_length=40)),
                ('qualification', models.CharField(default='', max_length=40)),
                ('specialization', models.CharField(default='', max_length=40)),
                ('dob', models.DateField(default=datetime.date(2022, 1, 16))),
                ('phone_no', models.CharField(default='', max_length=12)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1)),
                ('registration_no', models.CharField(default='', max_length=6)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
