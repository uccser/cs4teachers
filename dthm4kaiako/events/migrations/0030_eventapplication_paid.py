# Generated by Django 2.1.5 on 2021-02-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_eventapplication_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventapplication',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
