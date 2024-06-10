# Generated by Django 5.0.2 on 2024-02-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_branch_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='stock_deduction_type',
            field=models.CharField(choices=[('MA', 'MA'), ('FIFO', 'FIFO')], default='MA', max_length=4),
        ),
    ]
