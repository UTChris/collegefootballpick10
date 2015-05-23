# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conf_name', models.CharField(max_length=40)),
                ('div_name', models.CharField(max_length=40, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '1. Conferences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_year', models.IntegerField(default=2015)),
                ('game_week', models.IntegerField(default=1)),
                ('game_num', models.IntegerField(default=0)),
                ('team1_actual_points', models.IntegerField(default=-1)),
                ('team2_actual_points', models.IntegerField(default=-1)),
                ('favored', models.IntegerField(default=0)),
                ('spread', models.IntegerField(default=0)),
                ('game_state', models.IntegerField(default=0)),
                ('quarter', models.CharField(default=b'1st', max_length=3)),
                ('time_left', models.CharField(default=b'15:00', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '3. Games',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_winner', models.IntegerField(default=0)),
                ('team1_predicted_points', models.IntegerField(default=-1)),
                ('team2_predicted_points', models.IntegerField(default=-1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('pick_game', models.ForeignKey(to='pick10.Game')),
                ('pick_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '5. Picks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=40)),
                ('mascot', models.CharField(max_length=40)),
                ('current', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('conference', models.ForeignKey(default=None, to='pick10.Conference')),
            ],
            options={
                'verbose_name_plural': '2. Teams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week_year', models.IntegerField()),
                ('week_num', models.IntegerField()),
                ('lock_picks', models.BooleanField(default=False)),
                ('lock_scores', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('winner', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Weeks',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pick',
            name='pick_week',
            field=models.ForeignKey(to='pick10.Week'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(related_name=b'team1', to='pick10.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(related_name=b'team2', to='pick10.Team'),
            preserve_default=True,
        ),
    ]
