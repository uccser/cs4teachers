# Generated by Django 2.1.5 on 2019-02-15 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190130_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=12),
        ),
    ]