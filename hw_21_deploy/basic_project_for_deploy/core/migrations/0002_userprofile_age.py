# Generated by Django 5.0.7 on 2024-12-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
