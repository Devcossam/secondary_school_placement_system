# Generated by Django 5.1 on 2024-09-13 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_application_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='occupation',
            new_name='province',
        ),
        migrations.RemoveField(
            model_name='application',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='application',
            name='state_province',
        ),
    ]
