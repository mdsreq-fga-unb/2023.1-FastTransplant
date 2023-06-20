# Generated by Django 4.2.2 on 2023-06-19 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_pacient_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donator',
            name='age_50_60',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='anti_hbc',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='anti_hbs',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='anti_hcv',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='avch_death',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='chagas',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='cr_in',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='cr_in_greater_than_15',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='cr_out',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='hbsag',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='hiv',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='hltv',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='hypertension',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='name',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='toxoplasmosis',
        ),
        migrations.RemoveField(
            model_name='donator',
            name='vdrl',
        ),
        migrations.RemoveField(
            model_name='organreport',
            name='date',
        ),
        migrations.AddField(
            model_name='organreport',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='donator',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]
