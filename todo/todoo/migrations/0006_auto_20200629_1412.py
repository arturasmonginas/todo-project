# Generated by Django 3.0.7 on 2020-06-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0005_todo_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
    ]
