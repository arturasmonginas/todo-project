# Generated by Django 3.0.7 on 2020-06-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0010_remove_profile_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
