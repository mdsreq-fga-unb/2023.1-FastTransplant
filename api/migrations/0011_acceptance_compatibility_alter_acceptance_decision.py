# Generated by Django 4.2.2 on 2023-07-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_acceptance_decision'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptance',
            name='compatibility',
            field=models.CharField(choices=[('C', 'Compatível'), ('I', 'Incompatível')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='acceptance',
            name='decision',
            field=models.CharField(choices=[('A', 'Aceito'), ('R', 'Rejeitado')], default='A', max_length=1),
        ),
    ]
