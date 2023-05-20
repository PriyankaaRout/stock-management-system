# Generated by Django 3.0 on 2022-11-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0012_product_items_bought'),
    ]

    operations = [
        migrations.CreateModel(
            name='retailerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ret_name', models.CharField(max_length=30)),
                ('p_sku', models.CharField(max_length=10)),
                ('p_name', models.CharField(max_length=30)),
                ('p_quantity', models.IntegerField(blank=True)),
                ('date', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]