# Generated by Django 3.0.7 on 2020-06-29 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0009_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]