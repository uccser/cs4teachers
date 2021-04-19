# Generated by Django 2.2.18 on 2021-04-14 09:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0009_auto_20200309_2200'),
        ('events', '0018_migrate_organisers_to_entities'),
    ]

    operations = [
        migrations.CreateModel(
            name='AraAkoEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ara_ako_event', to='events.Event', verbose_name='Event')),
            ],
            options={
                'ordering': ['-event__start'],
            },
        ),
        migrations.CreateModel(
            name='AraAkoTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='ara_ako.AraAkoEvent', verbose_name='Ara Ako teams')),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ara_ako_team', to='resources.Resource', verbose_name='Ara Ako team resource')),
            ],
        ),
    ]
