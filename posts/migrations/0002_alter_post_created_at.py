# Generated by Django 5.1.2 on 2024-12-18 15:58

import django.utils.timezone
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
    ]
