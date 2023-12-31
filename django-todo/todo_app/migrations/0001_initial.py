# Generated by Django 4.2.5 on 2023-09-22 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='full text to do')),
                ('start_time', models.DateField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('status', models.CharField(choices=[('n', 'not yet'), ('o', 'done'), ('a', 'active')], max_length=15, verbose_name='Status')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'db_table': 'todo_list',
                'ordering': ['start_time', 'title'],
            },
        ),
    ]
