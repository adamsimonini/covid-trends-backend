# Generated by Django 3.2.2 on 2022-02-11 15:37

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forward_Sortation_Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('health_regions', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None)),
            ],
            options={
                'db_table': 'forward_sortation_area',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=150)),
                ('name_fr', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_code', models.PositiveSmallIntegerField()),
                ('alpha_code', models.CharField(max_length=2)),
                ('name_en', models.CharField(max_length=150)),
                ('name_fr', models.CharField(max_length=150)),
                ('fk_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_api.region')),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.CreateModel(
            name='Health_Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_uid', models.PositiveSmallIntegerField()),
                ('name_en', models.CharField(max_length=150)),
                ('name_fr', models.CharField(max_length=150)),
                ('website_en', models.CharField(max_length=300)),
                ('website_fr', models.CharField(max_length=300)),
                ('fk_province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_api.province')),
            ],
            options={
                'db_table': 'health_region',
            },
        ),
    ]
