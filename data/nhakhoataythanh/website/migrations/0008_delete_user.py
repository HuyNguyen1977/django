# Generated by Django 4.0.1 on 2022-02-08 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_customer_id_alter_groupuser_id_alter_job_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
