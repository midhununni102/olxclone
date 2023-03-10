# Generated by Django 4.1.2 on 2023-02-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0008_delete_image_products_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='product',
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('SPORTS', 'SPORTS'), ('FURNITURES', 'FURNITURES'), ('ELECTRONICS', 'ELECTRONICS'), ('MOBILES', 'MOBILES'), ('OTHERS', 'OTHERS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
