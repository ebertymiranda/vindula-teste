# Generated by Django 3.2.23 on 2023-11-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='data_assistido',
            field=models.DateField(blank=True, null=True),
        ),
    ]
