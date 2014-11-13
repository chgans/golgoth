# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import search.models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dork',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('query', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', search.models.CampaignNameField(max_length=32, unique=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dork',
            name='campaign',
            field=models.ForeignKey(default=1, to='search.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='dork',
            unique_together=set([('campaign', 'query')]),
        ),
        migrations.AddField(
            model_name='dork',
            name='created',
            field=model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dork',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dork',
            name='query',
            field=search.models.DorkQueryField(max_length=256),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=1024)),
                ('summary', models.TextField()),
                ('url', models.URLField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dork', models.ForeignKey(to='search.Dork')),
                ('result_set', models.ManyToManyField(to='search.Result')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('title', 'summary', 'url')]),
        ),
    ]
