# Generated by Django 3.0.5 on 2020-04-25 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200426_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 18, 44, 52, 832718)),
        ),
    ]