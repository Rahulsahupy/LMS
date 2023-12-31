# Generated by Django 4.1.7 on 2023-08-07 13:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seekho_app', '0018_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='data',
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seekho_app.course'),
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 7, 12, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
