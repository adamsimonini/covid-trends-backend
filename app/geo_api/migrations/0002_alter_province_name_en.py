# Generated by Django 3.2.2 on 2022-02-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='name_en',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
