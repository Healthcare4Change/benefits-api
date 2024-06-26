# Generated by Django 4.0.5 on 2023-04-14 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0051_programeligibilitysnapshot_new"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="household_member",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="expenses",
                to="screener.householdmember",
            ),
        ),
    ]
