# Generated by Django 4.1 on 2022-09-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_user',
            name='Name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='reg_user',
            name='Password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='reg_user',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
