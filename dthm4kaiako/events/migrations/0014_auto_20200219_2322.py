# Generated by Django 2.1.5 on 2020-02-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20190726_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='show_schedule',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='show_schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Northland region'), (2, 'Auckland region'), (3, 'Waikato region'), (4, 'Bay of Plenty region'), (5, 'Gisborne region'), (6, "Hawke's Bay region"), (7, 'Taranaki region'), (8, 'Manawatu-Wanganui region'), (9, 'Wellington region'), (10, 'Tasman region'), (11, 'Nelson region'), (12, 'Marlborough region'), (13, 'West Coast region'), (14, 'Canterbury region'), (15, 'Otago region'), (16, 'Southland region'), (17, 'Chatman Islands')], default=14),
        ),
    ]
