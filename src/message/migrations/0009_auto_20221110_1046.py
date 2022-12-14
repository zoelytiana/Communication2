# Generated by Django 3.2 on 2022-11-10 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0008_auto_20221109_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ordinateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='ref',
        ),
        migrations.AddField(
            model_name='message',
            name='autres',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='acces',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='message.acces'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='employe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='message.employe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='ordinateur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='message.ordinateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='telephone',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='message.telephone'),
            preserve_default=False,
        ),
    ]
