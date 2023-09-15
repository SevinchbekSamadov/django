# Generated by Django 4.2.3 on 2023-09-15 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viloyat',
            fields=[
                ('viloyat_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('viloyat', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='Tuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tuman_uz', models.CharField(max_length=255)),
                ('tuman_en', models.CharField(max_length=255)),
                ('tuman_ru', models.CharField(max_length=255)),
                ('tumen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_districts.viloyat')),
            ],
            options={
                'db_table': 'tumanlar',
            },
        ),
    ]
