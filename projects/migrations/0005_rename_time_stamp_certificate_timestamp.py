# Generated by Django 4.2.3 on 2024-09-04 00:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_alter_certificate_time_stamp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="certificate",
            old_name="time_stamp",
            new_name="timestamp",
        ),
    ]
