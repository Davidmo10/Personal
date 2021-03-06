# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=500)),
                ('ans', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GameDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('on', models.BooleanField(default=False)),
                ('winner', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Hunt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_order', models.IntegerField(default=-1)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.GameDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=100)),
                ('wrong', models.FloatField(default=-10)),
                ('right', models.FloatField(default=50)),
                ('place_numerator', models.FloatField(default=100)),
                ('ans_per_sec', models.FloatField(default=-0.1)),
                ('game_per_sec', models.FloatField(default=-1e-05)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur', models.IntegerField(default=0)),
                ('pending', models.DateTimeField(default=None, null=True)),
                ('playing', models.BooleanField(default=False)),
                ('score', models.FloatField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.GameDetails')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('is_mkr', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
        migrations.AddField(
            model_name='hunt',
            name='lmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Landmark'),
        ),
        migrations.AddField(
            model_name='gamedetails',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.User'),
        ),
        migrations.AddField(
            model_name='gamedetails',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.ScoreScheme'),
        ),
        migrations.AddField(
            model_name='confirmation',
            name='lmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Landmark'),
        ),
        migrations.AddField(
            model_name='clue',
            name='lmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Landmark'),
        ),
    ]
