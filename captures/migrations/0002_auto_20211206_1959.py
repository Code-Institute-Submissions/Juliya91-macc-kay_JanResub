# Generated by Django 3.2.9 on 2021-12-06 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('captures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='website_url',
        ),
    ]