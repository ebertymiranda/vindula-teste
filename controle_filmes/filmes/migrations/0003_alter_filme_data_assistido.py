# Generated by Django 3.2.23 on 2023-11-23 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0002_alter_filme_data_assistido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='data_assistido',
            field=models.DateField(),
        ),
    ]
