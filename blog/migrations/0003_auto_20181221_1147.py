# Generated by Django 2.1.4 on 2018-12-21 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181221_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 21, 3, 47, 15, 397063, tzinfo=utc)),
        ),
    ]