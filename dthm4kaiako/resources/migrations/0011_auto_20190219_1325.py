# Generated by Django 2.1.5 on 2019-02-19 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20190219_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nzqastandard',
            options={'ordering': ['level', 'abbreviation'], 'verbose_name': 'NZQA standard'},
        ),
    ]
