# Generated by Django 3.2 on 2022-11-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0009_auto_20221110_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='acces',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='employe',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='ordinateur',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
