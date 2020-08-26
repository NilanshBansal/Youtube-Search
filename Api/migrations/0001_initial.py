# Generated by Django 3.1 on 2020-08-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=700, null=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('publishedDateTime', models.DateTimeField()),
                ('thumbnailsUrls', models.URLField()),
                ('channel_id', models.CharField(blank=True, max_length=500, null=True)),
                ('channel_title', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
