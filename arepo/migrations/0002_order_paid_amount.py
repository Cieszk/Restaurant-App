# Generated by Django 2.2.7 on 2019-11-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arepo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_amount',
            field=models.IntegerField(default=0),
        ),
    ]
