# Generated by Django 5.1.2 on 2024-11-17 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_delete_person_alter_comment_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.ad'),
        ),
    ]
