# Generated by Django 2.1.5 on 2020-03-09 09:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200307_2336'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0008_resource_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='author_entities',
            field=models.ManyToManyField(blank=True, related_name='resources', to='users.Entity'),
        ),
        migrations.AddField(
            model_name='resource',
            name='author_users',
            field=models.ManyToManyField(blank=True, related_name='resources', to=settings.AUTH_USER_MODEL),
        ),
    ]
