# Generated by Django 3.0 on 2022-10-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0004_auto_20221007_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
