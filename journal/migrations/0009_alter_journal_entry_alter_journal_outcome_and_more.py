# Generated by Django 5.0.6 on 2024-07-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_journal_note_delete_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='entry',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='outcome',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='stop_loss',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
