# Generated by Django 3.2.5 on 2021-07-08 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contact_booktags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='booktags',
        ),
    ]