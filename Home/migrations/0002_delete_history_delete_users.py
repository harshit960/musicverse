# Generated by Django 4.1 on 2022-09-07 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='history',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
