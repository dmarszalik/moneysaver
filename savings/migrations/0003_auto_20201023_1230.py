# Generated by Django 3.1.2 on 2020-10-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0002_aim_is_finished'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aim',
            old_name='is_finished',
            new_name='isFinished',
        ),
    ]