# Generated by Django 4.1.2 on 2023-02-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0005_image_alter_products_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='products',
            name='condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=200),
        ),
    ]