# Generated by Django 5.0.6 on 2024-05-12 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access_keys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_email', models.EmailField(max_length=254)),
                ('institution_name', models.CharField(max_length=254)),
                ('key', models.BooleanField(default=True)),
                ('linked_access_key', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='access_keys.access_key')),
            ],
        ),
    ]
