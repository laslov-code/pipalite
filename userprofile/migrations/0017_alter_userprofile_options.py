# Generated by Django 5.0.2 on 2024-05-03 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_alter_userprofile_branch_alter_userprofile_company_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_modify_role', 'Can modify own role.'), ('can_view_users', 'Can view other users.'), ('can_modify_users', 'Can modify other users'))},
        ),
    ]
