# Generated by Django 3.0 on 2022-10-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0010_auto_20221017_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(max_length=200, null=True, upload_to='photos'),
        ),
    ]
