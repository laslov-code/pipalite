# Generated by Django 5.0.2 on 2024-02-18 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('userprofile', '0012_remove_userprofile_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='warehouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
        ),
    ]
