# Generated by Django 3.2.7 on 2022-12-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0012_auto_20221120_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='challenge_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
