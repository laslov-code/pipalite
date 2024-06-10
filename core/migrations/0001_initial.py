# Generated by Django 5.0.2 on 2024-02-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(default='company/default.png', upload_to='company')),
                ('tagline', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('tax_id', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_num', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
