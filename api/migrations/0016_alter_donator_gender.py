# Generated by Django 4.2.2 on 2023-07-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_donator_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donator',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
