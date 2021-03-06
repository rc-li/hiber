# Generated by Django 2.1.7 on 2019-02-26 17:58

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import hiber.apps.bathouse.models


class Migration(migrations.Migration):

    dependencies = [
        ('bathouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bat',
            name='common_name',
            field=models.CharField(help_text='Name used in everyday life', max_length=255),
        ),
        migrations.AlterField(
            model_name='bat',
            name='habits',
            field=hiber.apps.bathouse.models.ChoiceArrayField(base_field=models.CharField(choices=[('HI', 'Hibernates'), ('MI', 'Migrates'), ('CR', 'Cave roosts'), ('TR', 'Tree roosts')], max_length=2), blank=True, help_text='What the species tends to do in order to survive', size=None),
        ),
        migrations.AlterField(
            model_name='bat',
            name='pups',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(help_text='Typical offspring per year'),
        ),
        migrations.AlterField(
            model_name='bat',
            name='rarity',
            field=models.CharField(choices=[('CO', 'Common'), ('SC', 'Seasonally Common'), ('RA', 'Rare')], default='CO', help_text='How often the species is seen', max_length=2),
        ),
        migrations.AlterField(
            model_name='bat',
            name='risk',
            field=hiber.apps.bathouse.models.ChoiceArrayField(base_field=models.CharField(choices=[('NT', 'Not threatened'), ('EN', 'Endangered'), ('TH', 'Threatened'), ('SC', 'Special concern')], max_length=2), blank=True, help_text='Conservation status for the species', size=None),
        ),
        migrations.AlterField(
            model_name='bat',
            name='risk_scope',
            field=hiber.apps.bathouse.models.ChoiceArrayField(base_field=models.CharField(choices=[('ST', 'State'), ('FE', 'Federally')], max_length=2, null=True), blank=True, help_text='Whether or not this applies at the federal or state level', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='bat',
            name='scientific_name',
            field=models.CharField(help_text='Formal system used for naming species', max_length=255),
        ),
        migrations.AlterField(
            model_name='bat',
            name='size',
            field=django.contrib.postgres.fields.ranges.FloatRangeField(help_text='Typical size in inches'),
        ),
    ]
