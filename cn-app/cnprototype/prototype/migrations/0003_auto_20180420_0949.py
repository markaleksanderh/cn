# Generated by Django 2.0.2 on 2018-04-20 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_auto_20180420_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='name'),
        ),
    ]
