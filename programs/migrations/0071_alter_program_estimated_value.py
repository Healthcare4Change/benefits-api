# Generated by Django 4.2.11 on 2024-05-06 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("translations", "0004_translation_no_auto"),
        ("programs", "0070_auto_20240506_1817"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="estimated_value",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="program_estimated_value",
                to="translations.translation",
            ),
        ),
    ]
