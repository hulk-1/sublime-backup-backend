# Generated by Django 2.2.3 on 2019-07-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0002_auto_20190712_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='original_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
