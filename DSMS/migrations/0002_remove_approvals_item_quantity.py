# Generated by Django 4.0.6 on 2022-08-25 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DSMS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvals',
            name='item_quantity',
        ),
    ]
