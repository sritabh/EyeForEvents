# Generated by Django 3.2.3 on 2021-05-20 09:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20210520_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 9, 46, 14, 677930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(null=True, upload_to='events/53dc17df-1af4-48de-b32d-4015b8da1374'),
        ),
        migrations.AlterField(
            model_name='event',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 20, 9, 46, 14, 677930, tzinfo=utc)),
        ),
    ]