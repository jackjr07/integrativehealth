# Generated by Django 3.2.7 on 2021-09-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vascularbridge', '0004_auto_20210917_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='limbIndexSym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acuteOnTop', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='vascularbridgeregister',
            name='limbIndexSide',
        ),
        migrations.AddField(
            model_name='vascularbridgeregister',
            name='leftLimbIndex',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'Right'), ('both', 'Both')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='limbIndex',
        ),
        migrations.AddField(
            model_name='vascularbridgeregister',
            name='rightLimbIndex',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='vascularbridge.limbindexsym'),
            preserve_default=False,
        ),
    ]
