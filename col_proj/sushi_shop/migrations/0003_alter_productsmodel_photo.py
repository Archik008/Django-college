# Generated by Django 5.1.7 on 2025-03-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sushi_shop', '0002_alter_productsmodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
