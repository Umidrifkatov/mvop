# Generated by Django 3.1.7 on 2021-05-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_patient_soe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]