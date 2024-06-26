# Generated by Django 4.0.5 on 2023-09-05 22:20

from django.db import migrations
from django.conf import settings


def migrate_translations(apps, schema_editor):
    Program = apps.get_model("programs", "Program")
    Translation = apps.get_model("translations", "Translation")

    translated_fields = (
        "description_short",
        "name",
        "description",
        "learn_more_link",
        "apply_button_link",
        "value_type",
        "estimated_delivery_time",
        "estimated_application_time",
        "category",
    )
    non_translated_fields = ("active", "legal_status_required", "name_abbreviated")
    for program in Program.objects.all():
        for field in translated_fields:
            translation = Translation.objects.add_translation(
                f"program.{program.name_abbreviated}_{program.id}-{field}", getattr(program, field)
            )
            setattr(program, field + "_1", translation)
            for lang in settings.PARLER_LANGUAGES[None]:
                program.set_current_language(lang["code"])
                Translation.objects.edit_translation(
                    f"program.{program.name_abbreviated}_{program.id}-{field}",
                    lang["code"],
                    getattr(program, field),
                    True,
                )
        for field in non_translated_fields:
            setattr(program, field + "_1", getattr(program, field))
        program.save()


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0041_remove_referrer_logo_remove_referrer_white_label_css_and_more"),
        ("translations", "0003_alter_translation_managers"),
    ]

    operations = [migrations.RunPython(migrate_translations)]
