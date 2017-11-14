# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=70)),
                ('year', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
                ('mileage', models.IntegerField(default=0)),
                ('mpg', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('displacement', models.IntegerField(default=100)),
                ('family', models.CharField(max_length=100)),
                ('horsepower', models.IntegerField(default=10)),
                ('rpm', models.IntegerField(default=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cardescription',
            name='motor',
            field=models.OneToOneField(to='it4045app.Motor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cardescription',
            name='transmission',
            field=models.OneToOneField(to='it4045app.Transmission'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.OneToOneField(to='it4045app.CarDescription'),
            preserve_default=True,
        ),
    ]
