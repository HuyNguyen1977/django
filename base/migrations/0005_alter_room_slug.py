# Generated by Django 4.0 on 2022-01-20 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_slug_alter_room_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
