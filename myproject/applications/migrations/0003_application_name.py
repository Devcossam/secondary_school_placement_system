# Generated by Django 5.1 on 2024-09-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_application_address_application_age_application_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]