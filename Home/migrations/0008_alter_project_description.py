# Generated by Django 5.2 on 2025-07-03 21:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
