# Generated by Django 4.0.5 on 2022-08-10 20:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="cell",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+17202373591", max_length=128, region=None, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="email_or_cell",
            field=models.CharField(default="bhiatt@garycommunity.org", max_length=320, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="email address"),
        ),
    ]
