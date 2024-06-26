# Generated by Django 5.0.2 on 2024-04-28 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_branch_header_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.company')),
                ('page_content_number', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
