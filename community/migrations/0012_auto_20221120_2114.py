# Generated by Django 3.2.7 on 2022-11-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_auto_20221120_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='f',
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(),
        ),
    ]
