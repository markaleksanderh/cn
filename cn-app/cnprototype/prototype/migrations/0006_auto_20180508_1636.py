# Generated by Django 2.0.4 on 2018-05-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0005_quote_job_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='job_name',
            field=models.CharField(help_text='Enter job name', max_length=200, null=True),
        ),
    ]