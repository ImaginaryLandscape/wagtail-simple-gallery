# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-06 13:05
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def forwards(apps, schema_editor):
    if not settings.WAGTAILIMAGES_IMAGE_MODEL or settings.WAGTAILIMAGES_IMAGE_MODEL == 'wagtailimages.Image':
        try:
            OldModel = apps.get_model('wagtailimages', 'Image')
        except LookupError:
            return

        NewModel = apps.get_model('wagtail_simple_gallery', 'CustomImage')
        NewModel.objects.bulk_create(
            NewModel(id=old_obj.id, title=old_obj.title, file=old_obj.file, created_at=old_obj.created_at)
            for old_obj in OldModel.objects.all()
        )
    else:
        print('Default wagtail image model is not in use, nothing to do here.')
    return


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_simple_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
