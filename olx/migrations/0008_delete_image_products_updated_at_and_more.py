# Generated by Django 4.1.2 on 2023-02-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0007_remove_products_image_products_photo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(choices=[('SPORTS', 'SPORTS'), ('FURNITURES', 'FURNITURES'), ('ELECTRONICS', 'ELECTRONICS'), ('MOBILES', 'MOBILES'), ('OTHERS', 'OTHERS')], max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
