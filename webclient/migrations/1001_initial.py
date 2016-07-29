# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 02:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='unknown', max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImageLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelShapes', models.TextField(max_length=10000)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('categoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.CategoryType')),
                ('parentImage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.Image')),
            ],
        ),
        migrations.CreateModel(
            name='ImageSourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='unknown', max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.ImageSourceType'),
        ),
    ]