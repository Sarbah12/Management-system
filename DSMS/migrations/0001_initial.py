# Generated by Django 4.0.6 on 2022-08-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name=str)),
                ('item_quantity', models.IntegerField(max_length=90, verbose_name=int)),
            ],
        ),
    ]
