# Generated by Django 4.2.2 on 2023-06-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_donator_age_50_60_remove_donator_anti_hbc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donator',
            name='rgct',
            field=models.CharField(max_length=100),
        ),
    ]
