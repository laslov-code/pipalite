# Generated by Django 5.0.2 on 2024-02-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='/home/cody/Codes/pipalite/pipalite/images/avatars/default.png', null=True, upload_to='avatars'),
        ),
    ]
