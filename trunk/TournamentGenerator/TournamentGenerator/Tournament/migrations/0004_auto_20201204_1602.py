# Generated by Django 3.1.3 on 2020-12-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0003_auto_20201204_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='TournamentSize',
            field=models.IntegerField(choices=[(8, '8 Teams'), (16, '16 Teams'), (32, '32 Teams')]),
        ),
    ]
