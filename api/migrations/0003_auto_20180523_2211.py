# Generated by Django 2.0.5 on 2018-05-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180523_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='available_at',
            field=models.DateTimeField(verbose_name='available_at'),
        ),
    ]
