# Generated by Django 2.0.2 on 2018-04-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0003_company_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='added',
            field=models.DateField(blank=True, null=True),
        ),
    ]
