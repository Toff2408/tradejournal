# Generated by Django 5.0.6 on 2024-07-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_alter_note_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='note',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
