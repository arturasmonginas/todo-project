# Generated by Django 3.0.7 on 2020-06-29 08:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoo', '0002_auto_20200611_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
