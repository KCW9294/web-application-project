# Generated by Django 4.2 on 2023-07-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='is_working',
            field=models.BooleanField(default=True),
        ),
    ]