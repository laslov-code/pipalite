# Generated by Django 5.0.2 on 2024-02-23 14:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_company_stock_deduction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
