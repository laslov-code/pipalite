# Generated by Django 5.0.2 on 2024-04-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='page_content_number',
            field=models.PositiveIntegerField(default=5, null=True),
        ),
    ]
