# Generated by Django 5.1.2 on 2024-11-17 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.ad'),
        ),
    ]
