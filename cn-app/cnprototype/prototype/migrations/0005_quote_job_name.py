# Generated by Django 2.0.4 on 2018-05-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0004_auto_20180508_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='job_name',
            field=models.CharField(default=None, help_text='Enter job name', max_length=200),
            preserve_default=False,
        ),
    ]