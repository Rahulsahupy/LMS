# Generated by Django 4.1.7 on 2023-07-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seekho_app', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]