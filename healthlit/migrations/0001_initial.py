# Generated by Django 3.0.5 on 2021-09-14 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programName', models.CharField(max_length=60, verbose_name='Name of the program')),
                ('programDescription', models.TextField(verbose_name='Description of the program')),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]