# Generated by Django 4.1.7 on 2023-08-04 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekho_app', '0012_alter_video_time_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
            ],
        ),
    ]
