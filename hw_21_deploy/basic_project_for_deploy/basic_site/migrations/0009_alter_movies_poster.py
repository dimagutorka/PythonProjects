# Generated by Django 5.1.3 on 2024-12-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_site', '0008_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, default='movie_posters/default-poster.jpg', null=True, upload_to='movie_posters/'),
        ),
    ]
