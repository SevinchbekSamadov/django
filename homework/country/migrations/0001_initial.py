# Generated by Django 4.2.3 on 2023-09-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='country_name')),
                ('population', models.IntegerField(verbose_name='population')),
                ('area', models.FloatField(verbose_name='area of country')),
                ('density', models.FloatField(verbose_name='density of country')),
            ],
            options={
                'db_table': 'countries',
            },
        ),
    ]