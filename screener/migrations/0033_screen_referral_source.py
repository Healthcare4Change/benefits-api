# Generated by Django 4.0.5 on 2022-09-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0032_message_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="screen",
            name="referral_source",
            field=models.CharField(blank=True, default=None, max_length=320, null=True),
        ),
    ]
