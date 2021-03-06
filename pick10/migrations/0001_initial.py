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
                'verbose_name_plural': '4. Conferences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gamenum', models.IntegerField(default=0)),
                ('team1_actual_points', models.IntegerField(default=-1)),
                ('team2_actual_points', models.IntegerField(default=-1)),
                ('favored', models.IntegerField(default=0)),
                ('spread', models.DecimalField(default=0.0, max_digits=4, decimal_places=1)),
                ('kickoff', models.DateTimeField(null=True, blank=True)),
                ('game_state', models.IntegerField(default=0)),
                ('quarter', models.CharField(default=b'1st', max_length=3)),
                ('time_left', models.CharField(default=b'15:00', max_length=10)),
                ('winner', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '7. Games',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('winner', models.IntegerField(default=0)),
                ('team1_predicted_points', models.IntegerField(default=-1)),
                ('team2_predicted_points', models.IntegerField(default=-1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('game', models.ForeignKey(to='pick10.Game')),
            ],
            options={
                'verbose_name_plural': '8. Picks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_name', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('private_name', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('ss_name', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '2. Players',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('player', models.ForeignKey(to='pick10.Player')),
            ],
            options={
                'verbose_name_plural': '3. PlayerYears',
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
                'verbose_name_plural': '5. Teams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50, blank=True)),
                ('preferredtz', models.CharField(blank=True, max_length=100, null=True, choices=[(b'US/Alaska', b'US/Alaska'), (b'US/Aleutian', b'US/Aleutian'), (b'US/Arizona', b'US/Arizona'), (b'US/Central', b'US/Central'), (b'US/East-Indiana', b'US/East-Indiana'), (b'US/Eastern', b'US/Eastern'), (b'US/Hawaii', b'US/Hawaii'), (b'US/Indiana-Starke', b'US/Indiana-Starke'), (b'US/Michigan', b'US/Michigan'), (b'US/Mountain', b'US/Mountain'), (b'US/Pacific', b'US/Pacific'), (b'US/Pacific-New', b'US/Pacific-New'), (b'US/Samoa', b'US/Samoa')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('player', models.OneToOneField(null=True, blank=True, to='pick10.Player')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weeknum', models.IntegerField()),
                ('lock_picks', models.DateTimeField(null=True, blank=True)),
                ('lock_scores', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('winner', models.ForeignKey(default=None, blank=True, to='pick10.Player', null=True)),
            ],
            options={
                'verbose_name_plural': '6. Weeks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yearnum', models.IntegerField()),
                ('entry_fee', models.DecimalField(default=10.0, max_digits=6, decimal_places=2)),
                ('payout_week', models.DecimalField(default=15.0, max_digits=6, decimal_places=2)),
                ('payout_first', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('payout_second', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('payout_third', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '1. Years',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='week',
            name='year',
            field=models.ForeignKey(to='pick10.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeryear',
            name='year',
            field=models.ForeignKey(to='pick10.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pick',
            name='player',
            field=models.ForeignKey(to='pick10.Player'),
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
        migrations.AddField(
            model_name='game',
            name='week',
            field=models.ForeignKey(to='pick10.Week'),
            preserve_default=True,
        ),
    ]
