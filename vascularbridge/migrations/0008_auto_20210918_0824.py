# Generated by Django 3.2.7 on 2021-09-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vascularbridge', '0007_rename_limbindex_limbindexsym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='limbindexsym',
            name='symptoms',
        ),
        migrations.AddField(
            model_name='limbindexsym',
            name='limbSymptoms',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
