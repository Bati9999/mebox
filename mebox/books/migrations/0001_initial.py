# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
