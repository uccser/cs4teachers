# Generated by Django 2.1.5 on 2019-07-30 09:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='pdf',
        ),
        migrations.AddField(
            model_name='resource',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
            preserve_default=False,
        ),
    ]
