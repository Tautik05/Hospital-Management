# Generated by Django 5.1 on 2024-11-20 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_initial'),
        ('hospital', '0003_patientrecord'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='departments',
            field=models.ManyToManyField(related_name='departments_available', to='accounts.department'),
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital'),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
    ]
