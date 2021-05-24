# Generated by Django 3.2.3 on 2021-05-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20210523_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='alt_contact_number',
            field=models.PositiveSmallIntegerField(verbose_name='alt_contact_number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact_number',
            field=models.PositiveSmallIntegerField(verbose_name='contact_number'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, default='events/event_default.jpg', upload_to='events/e6247e39-2521-49b0-b51d-847c142ea4c1'),
        ),
        migrations.AlterField(
            model_name='event',
            name='last_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]