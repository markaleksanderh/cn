# Generated by Django 2.0.4 on 2018-05-14 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0006_auto_20180508_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='closing_date',
        ),
        migrations.AddField(
            model_name='job',
            name='closing_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Enter ending date:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='job_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
