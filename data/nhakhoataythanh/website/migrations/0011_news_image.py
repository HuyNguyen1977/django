# Generated by Django 4.0.1 on 2022-02-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_news_image_newphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]