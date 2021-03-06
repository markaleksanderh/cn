# Generated by Django 2.0.4 on 2018-05-02 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prototype.Job')),
                ('quote_added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
