# Generated by Django 4.0.6 on 2022-07-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True, verbose_name='Tag')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50, verbose_name='URL')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('thumbnail', models.ImageField(upload_to='Thumbnails/', verbose_name='Thumbnail')),
                ('tag', models.ManyToManyField(related_name='youtubeVideo', to='youtubeAPI.videotag', verbose_name='Tag')),
            ],
        ),
    ]
