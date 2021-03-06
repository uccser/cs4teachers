# Generated by Django 2.1.5 on 2019-07-30 22:24

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_outcome_number', models.PositiveSmallIntegerField(default=1)),
                ('code', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('short_label', models.CharField(max_length=10)),
                ('learning_area', models.CharField(max_length=100)),
                ('learning_area_code', models.CharField(max_length=10)),
                ('technological_area', models.CharField(max_length=100)),
                ('technological_area_code', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('target_progress_outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='poet.ProgressOutcome')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField()),
                ('progress_outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='poet.ProgressOutcome')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='poet.Resource')),
            ],
        ),
    ]
