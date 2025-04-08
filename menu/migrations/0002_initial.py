# Generated by Django 5.2 on 2025-04-08 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysrolemenu',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='role.sysrole'),
        ),
    ]
