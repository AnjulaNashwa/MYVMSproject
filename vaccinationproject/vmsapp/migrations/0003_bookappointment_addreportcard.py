# Generated by Django 4.2.7 on 2024-01-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsapp', '0002_vaccinationcard_addreportcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='addreportcard',
            field=models.IntegerField(default=0),
        ),
    ]
