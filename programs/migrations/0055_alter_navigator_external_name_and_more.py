# Generated by Django 4.0.5 on 2023-09-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0054_navigator_external_name_program_external_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigator",
            name="external_name",
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="program",
            name="external_name",
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="urgentneed",
            name="external_name",
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
