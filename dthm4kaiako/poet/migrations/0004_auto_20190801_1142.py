# Generated by Django 2.1.5 on 2019-07-31 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0003_auto_20190731_1912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progressoutcome',
            options={'ordering': ['short_label']},
        ),
    ]
