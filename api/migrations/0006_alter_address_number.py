# Generated by Django 4.0.3 on 2022-03-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_address_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.IntegerField(),
        ),
    ]
