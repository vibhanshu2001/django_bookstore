# Generated by Django 3.2.5 on 2021-07-08 11:10

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('app', '0002_auto_20210706_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]