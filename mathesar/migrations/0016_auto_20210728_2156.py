# Generated by Django 3.1.7 on 2021-07-28 21:56

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0015_datafile_header'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='database',
            managers=[
                ('current_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='schema',
            managers=[
                ('current_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='table',
            managers=[
                ('current_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='datafile',
            name='created_from',
            field=models.CharField(choices=[('FILE', 'File'), ('PASTE', 'Paste')], default='file', max_length=128),
            preserve_default=False,
        ),
    ]