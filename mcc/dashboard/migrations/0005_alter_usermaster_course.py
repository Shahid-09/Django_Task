# Generated by Django 5.0.3 on 2024-03-24 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_usermaster_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='course',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.coursemaster'),
        ),
    ]