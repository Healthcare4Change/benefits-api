# Generated by Django 4.0.5 on 2022-07-14 20:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0009_remove_householdmember_zipcode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="screen",
            name="age",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="disability_medicaid",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="disabled",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="has_expenses",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="has_income",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="medicaid",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="pregnant",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="student",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="student_full_time",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="unemployed",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="veteran",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="visually_impaired",
        ),
        migrations.RemoveField(
            model_name="screen",
            name="worked_in_last_18_mos",
        ),
    ]
