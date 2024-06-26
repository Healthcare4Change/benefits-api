# Generated by Django 4.0.5 on 2023-09-06 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("translations", "0003_alter_translation_managers"),
        ("programs", "0046_delete_programtranslation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="active_1",
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name="program",
            name="apply_button_link_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="apply_button_link",
                to="translations.translation",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="category_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="category", to="translations.translation"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="description_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="description", to="translations.translation"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="description_short_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="description_short",
                to="translations.translation",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="estimated_application_time_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="estimated_application_time",
                to="translations.translation",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="estimated_delivery_time_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="estimated_delivery_time",
                to="translations.translation",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="learn_more_link_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="learn_more_link",
                to="translations.translation",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="legal_status_required_1",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="program",
            name="name_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="name", to="translations.translation"
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="name_abbreviated_1",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="program",
            name="value_type_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="value_type", to="translations.translation"
            ),
        ),
    ]
