# Generated by Django 5.0.2 on 2024-02-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
