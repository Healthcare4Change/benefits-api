# Generated by Django 4.0.5 on 2022-06-30 19:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0004_rename_program_snapshot_program_description_short"),
    ]

    operations = [
        migrations.RenameField(
            model_name="program",
            old_name="program_name",
            new_name="name",
        ),
    ]
