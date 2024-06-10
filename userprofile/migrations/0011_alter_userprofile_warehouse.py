# Generated by Django 5.0.2 on 2024-02-18 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('userprofile', '0010_userprofile_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
    ]
