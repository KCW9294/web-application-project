# Generated by Django 4.2 on 2023-07-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='is_working',
            field=models.BooleanField(default=True),
        ),
    ]
