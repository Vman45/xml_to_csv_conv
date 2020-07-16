# Generated by Django 3.0.8 on 2020-07-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_request_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='export_csv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request',
            name='filename',
            field=models.CharField(default='compiled_xmls', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='save_csv',
            field=models.BooleanField(default=False),
        ),
    ]
