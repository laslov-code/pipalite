# Generated by Django 5.0.2 on 2024-02-18 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('userprofile', '0009_userprofile_birthdate_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='warehouse',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse'),
            preserve_default=False,
        ),
    ]
