# Generated by Django 4.0.5 on 2022-09-06 20:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0026_screen_filed_taxes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="screen",
            name="filed_taxes",
        ),
    ]
