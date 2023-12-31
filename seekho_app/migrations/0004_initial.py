# Generated by Django 4.1.7 on 2023-07-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seekho_app', '0003_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_profile', models.ImageField(upload_to='Media/author')),
                ('name', models.CharField(max_length=100, null=True)),
                ('about_author', models.TextField()),
            ],
        ),
    ]
