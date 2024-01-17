# Generated by Django 3.0.5 on 2022-11-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20221118_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='assignedNurseId',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDrugsId',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]