# Generated by Django 4.0.5 on 2023-04-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0052_alter_expense_household_member"),
    ]

    operations = [
        migrations.AlterField(
            model_name="householdmember",
            name="has_expenses",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="householdmember",
            name="has_income",
            field=models.BooleanField(null=True),
        ),
    ]
