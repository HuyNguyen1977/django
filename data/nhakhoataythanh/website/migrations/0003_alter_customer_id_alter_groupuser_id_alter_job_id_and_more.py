# Generated by Django 4.0.1 on 2022-02-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_topic_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='groupuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tiensubenh',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]