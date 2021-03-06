# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameD', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameP', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Presciption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Patient')),
            ],
            options={
                'verbose_name_plural': 'Presciptions',
            },
        ),
    ]
