# Generated by Django 4.0.5 on 2022-06-16 16:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0003_rename_type_incomestream_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incomestream",
            name="label",
        ),
    ]
